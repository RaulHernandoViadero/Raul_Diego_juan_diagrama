import json
import pydot


with open("example_backend.json", "r") as archivo:
    datos = json.load(archivo)

graph = pydot.Dot(graph_type='digraph')

for dato in datos:
    id_nodo = dato['id']
    schema_id = dato.get('schemaId', '')  
    node_label = f"{id_nodo}\n{schema_id}"  
    node = pydot.Node(id_nodo, label=schema_id) 
    graph.add_node(node)

for node_data in datos:
    for output_data in node_data.get('connectedTo', {}).get('outputs', []):
        edge = pydot.Edge(node_data['id'], output_data)
        graph.add_edge(edge)

graph.write_png('diagrama_flujo.png')
