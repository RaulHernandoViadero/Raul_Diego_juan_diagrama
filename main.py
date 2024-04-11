import json
import pydot

with open('example_backend.json', 'r') as archivo:
    datos = json.load(archivo)

for dato in datos:
    id_nodo = dato["id"]
    schemaID = dato["schemaId"]
    outputs = dato["connectedTo"]["outputs"]
    inputs = dato["connectedTo"]["inputs"]
    
    print("ID:", id_nodo)
    print("Outputs: ", outputs)
    print("Inputs:", inputs)



