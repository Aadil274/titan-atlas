from app.graph.graph_queries import get_node_dependencies, find_node

print(get_node_dependencies("OpenAI"))
print(find_node("openai"))
print(find_node("OPENAI"))
print(find_node("open ai"))