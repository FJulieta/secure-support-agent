from agent import agent

result = agent.invoke({
    "question": "¿Qué hago si falla la conexión VPN?",
    "documents": []
})

for document in result["documents"]:
    print("Fuente:", document["source"])
    print("Similitud:", round(document["score"], 3))
    print("Contenido:", document["content"])