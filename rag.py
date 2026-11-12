from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


RUNBOOKS_DIR = Path(__file__).resolve().parent / "runbooks"


def load_runbooks():
    """Carga los documentos Markdown."""

    documents = []

    for file in sorted(RUNBOOKS_DIR.glob("*.md")):
        documents.append({
            "source": file.name,
            "content": file.read_text(encoding="utf-8")
        })

    return documents


def retrieve(question, top_k=2):
    """Busca los runbooks más relevantes."""

    documents = load_runbooks()

    if not documents:
        return []

    # Convertimos los documentos en vectores
    texts = [doc["content"] for doc in documents]

    vectorizer = TfidfVectorizer()
    document_vectors = vectorizer.fit_transform(texts)

    # Convertimos la pregunta en un vector
    question_vector = vectorizer.transform([question])

    # Calculamos la similitud
    scores = cosine_similarity(
        question_vector,
        document_vectors
    )[0]

    # Ordenamos por relevancia
    indices = scores.argsort()[::-1][:top_k]

    return [
        {
            **documents[i],
            "score": float(scores[i])
        }
        for i in indices
        if scores[i] > 0
    ]