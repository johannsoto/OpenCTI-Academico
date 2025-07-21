import pandas as pd
import uuid
import json
import argparse

# Función para generar un bundle STIX desde un archivo Excel
def generar_bundle(excel_path, output_path):
    # Leer archivo Excel
    df = pd.read_excel(excel_path)

    # Estructura base del bundle STIX
    bundle = {
        "type": "bundle",
        "id": f"bundle--{uuid.uuid4()}",
        "objects": []
    }

    # Definición de marcado TLP:CLEAR
    marking_definition = {
        "type": "marking-definition",
        "spec_version": "2.1",
        "id": "marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9",
        "created": "2017-01-20T00:00:00.000Z",
        "definition_type": "tlp",
        "name": "TLP:CLEAR",
        "definition": {
            "tlp": "clear"
        }
    }

    # Agregar la definición de marcado
    bundle["objects"].append(marking_definition)

    # Crear objetos ipv4-addr
    for _, row in df.iterrows():
        ip = str(row["IP"]).strip()
        agent = str(row["agent.name"]).strip()

        ipv4_obj = {
            "id": f"ipv4-addr--{uuid.uuid4()}",
            "spec_version": "2.1",
            "x_opencti_score": 50,
            "value": ip,
            "x_opencti_id": str(uuid.uuid4()),
            "x_opencti_type": "IPv4-Addr",
            "type": "ipv4-addr",
            "labels": [
                "ip maliciosa",
                agent
            ],
            "object_marking_refs": [
                "marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9"
            ]
        }

        bundle["objects"].append(ipv4_obj)

    # Guardar archivo JSON
    with open(output_path, "w") as f:
        json.dump(bundle, f, indent=2)

    print(f"✅ Bundle STIX generado en: {output_path}")

# Uso por línea de comandos
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generar bundle STIX 2.1 desde Excel con IPs y agentes")
    parser.add_argument("--input", required=True, help="Ruta del archivo Excel (.xlsx)")
    parser.add_argument("--output", required=True, help="Ruta del archivo de salida JSON")

    args = parser.parse_args()
    generar_bundle(args.input, args.output)
