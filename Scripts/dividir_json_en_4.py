import json
import uuid


with open("datos_completos.json", "r") as f:
    datos = json.load(f)


marking = [obj for obj in datos["objects"] if obj["type"] == "marking-definition"]
otros = [obj for obj in datos["objects"] if obj["type"] != "marking-definition"]


chunk_size = len(otros) // 2
partes = [otros[i:i + chunk_size] for i in range(0, len(otros), chunk_size)]


if len(partes) > 2:
    partes[1].extend(partes.pop())


for i, parte in enumerate(partes):
    bundle = {
        "type": "bundle",
        "id": f"bundle--{uuid.uuid4()}",
        "objects": marking + parte
    }
    with open(f"datos_parte_{i+1}.json", "w") as f:
        json.dump(bundle, f, indent=2)

print("✅ Archivo dividido en 11 partes: datos_parte_1.json a datos_parte_11.json")
