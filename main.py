import json
import pydot

with open("/home/juanfm/formacion_python/Raul_Diego_juan_diagrama/example_backend.json", "r") as archivo:
    datos = json.load(archivo)

graph = pydot.Dot(graph_type='digraph')


for dato in datos:
    id_nodo = dato['id']
    node_label = f"{id_nodo}\n{dato.get('schemaId', '')}" 
    node = pydot.Node(id_nodo, label=node_label)
    graph.add_node(node)


for node_data in datos:
    for output_data in node_data.get('connectedTo', {}).get('outputs', []):
        edge = pydot.Edge(node_data['id'], output_data)
        graph.add_edge(edge)


graph.write_png('diagrama_flujo_opcion2.png')

