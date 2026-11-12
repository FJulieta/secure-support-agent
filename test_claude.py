
import os

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

# 1. Cargamos las variables del archivo .env
load_dotenv()

# 2. Configuramos el modelo de Claude
llm = ChatAnthropic(
    model="claude-haiku-4-5-20251001",
    max_tokens=100,
    api_key=os.environ["ANTHROPIC_API_KEY"],
)

# 3. Enviamos una pregunta de prueba
response = llm.invoke(
    "Respondé en español y en una sola oración: ¿qué es un runbook en soporte técnico?"
)

# 4. Mostramos la respuesta
print(response.content)
