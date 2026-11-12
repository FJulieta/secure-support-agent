
import re
import unicodedata
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


RUNBOOKS_DIR = Path(__file__).resolve().parent / "runbooks"

MIN_SIMILARITY = 0.10

STOPWORDS = [
    "a", "al", "ante", "como", "con", "de", "del",
    "el", "en", "es", "esta", "este", "hay",
    "la", "las", "lo", "los", "me", "mi", "no",
    "para", "por", "que", "se", "si", "su",
    "sus", "un", "una", "unos", "unas", "y",
    "yo", "debo", "hacer", "puedo", "necesito",
    "problema", "problemas", "usuario",
    "verificar", "revisar", "comprobar",
]

INJECTION_PATTERNS = [
    r"ignora(?:r)?\s+(?:todas?\s+)?(?:tus\s+)?instrucciones",
    r"respond[eé]\s+en\s+ingl[eé]s",
    r"establec[eé]\s+escalate",
    r"system\s+prompt",
    r"ignore\s+(?:all\s+)?previous\s+instructions",
]


def normalize_text(text):
    """Normaliza tildes y convierte a minúsculas."""

    text = text.lower()

    text = unicodedata.normalize("NFKD", text)

    return "".join(
        char for char in text
        if not unicodedata.combining(char)
    )


def clean_question(question):
    """Reduce la influencia de instrucciones sospechosas en RAG."""

    question = normalize_text(question)

    for pattern in INJECTION_PATTERNS:
        question = re.sub(
            pattern,
            " ",
            question,
            flags=re.IGNORECASE,
        )

    return question


def load_runbooks():
    """Carga los documentos Markdown."""

    documents = []

    for file in sorted(RUNBOOKS_DIR.glob("*.md")):
        documents.append({
            "source": file.name,
            "content": file.read_text(encoding="utf-8"),
        })

    return documents


def retrieve(question, top_k=2):
    """Recupera los runbooks más relevantes."""

    documents = load_runbooks()

    if not documents:
        return []

    texts = [
        normalize_text(
            doc["source"].replace(".md", " ")
            + "\n"
            + doc["content"]
        )
        for doc in documents
    ]

    vectorizer = TfidfVectorizer(
        stop_words=STOPWORDS,
        ngram_range=(1, 2),
        sublinear_tf=True,
    )

    document_vectors = vectorizer.fit_transform(texts)

    cleaned_question = clean_question(question)

    question_vector = vectorizer.transform(
        [cleaned_question]
    )

    scores = cosine_similarity(
        question_vector,
        document_vectors,
    )[0]

    indices = scores.argsort()[::-1][:top_k]

    return [
        {
            **documents[i],
            "score": float(scores[i]),
        }
        for i in indices
        if scores[i] >= MIN_SIMILARITY
    ]
