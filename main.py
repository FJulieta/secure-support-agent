from rag import retrieve

question = "¿Qué hago si falla la conexión VPN?"

results = retrieve(question)

if not results:
    print("No se encontraron documentos relevantes.")
else:
    for result in results:
        print("Fuente:", result["source"])
        print("Similitud:", round(result["score"], 3))
        print("Contenido:")
        print(result["content"])