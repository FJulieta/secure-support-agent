from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from rag import retrieve


# Estado que comparten los nodos del agente
class AgentState(TypedDict):
    question: str
    documents: list[dict]


# Primer nodo: recuperar documentación
def retrieve_documents(state: AgentState):
    question = state["question"]

    documents = retrieve(question)

    return {"documents": documents}


# Construcción del grafo
graph = StateGraph(AgentState)

graph.add_node("retrieve", retrieve_documents)

graph.add_edge(START, "retrieve")
graph.add_edge("retrieve", END)

agent = graph.compile()