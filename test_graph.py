
from agent import agent

question = (
    "¿Cuál es el procedimiento para recuperar una base de datos "
    "PostgreSQL eliminada accidentalmente?"
)

result = agent.invoke({
    "question": question,
    "documents": [],
    "answer": "",
    "sources": [],
    "escalate": False,
})

print("\nPREGUNTA:")
print(question)

print("\nRESPUESTA:")
print(result["answer"])

print("\nFUENTES:")
print(result["sources"])

print("\nESCALAR:")
print(result["escalate"])
