import json
import pydot


with open("/home/juanfm/formacion_python/Raul_Diego_juan_diagrama/example_backend.json", "r") as archivo:
    datos = json.load(archivo)

graph = pydot.Dot(graph_type='digraph')




