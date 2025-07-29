import pandas as pd
import uuid
import json


archivo_excel = "XDR - RCA GENERAL.xlsx"


df = pd.read_excel(archivo_excel)


stix_objects = []


stix_objects.append({
    "type": "marking-definition",
    "spec_version": "2.1",
    "id": "marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9",
    "created": "2017-01-20T00:00:00.000Z",
    "definition_type": "tlp",
    "name": "TLP:CLEAR",
    "definition": {
        "tlp": "clear"
    }
})


for _, row in df.iterrows():
    ip = str(row["IP"]).strip()
    label = str(row["agent.name"]).strip()

    stix_objects.append({
        "type": "ipv4-addr",
        "spec_version": "2.1",
        "id": f"ipv4-addr--{uuid.uuid4()}",
        "value": ip,
        "labels": ["ip maliciosa", label],
        "x_opencti_score": 50,
        "x_opencti_id": str(uuid.uuid4()),
        "x_opencti_type": "IPv4-Addr",
        "object_marking_refs": [
            "marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9"
        ]
    })


bundle = {
    "type": "bundle",
    "id": f"bundle--{uuid.uuid4()}",
    "objects": stix_objects
}


with open("datos_completos.json", "w") as f:
    json.dump(bundle, f, indent=2)

print("✅ Archivo datos_completos.json generado correctamente.")
