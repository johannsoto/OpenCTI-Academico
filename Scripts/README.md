# Generador de Bundle STIX 2.1 para OpenCTI

Este proyecto permite generar automáticamente un archivo STIX 2.1 en formato `.json` a partir de un archivo Excel que contenga indicadores de compromiso (IoCs), específicamente direcciones IP maliciosas con su origen o etiqueta asociada. El resultado está listo para ser importado en la plataforma **OpenCTI**.

---

## Objetivo

Facilitar la conversión de datos de inteligencia de amenazas en formato estructurado STIX 2.1 para integrarlos con OpenCTI, permitiendo una gestión más eficiente de indicadores como IPs maliciosas y su contexto.

---

## Estructura del Excel de entrada

El archivo debe contener dos columnas:

| IP              | agent.name         |
|-----------------|--------------------|
| xxx.xxx.xxx.xxx  | xxxxx    |
| xxx.xxx.xxx.xxx  | xxxxx    |

---

## Requisitos

- Python 3.8 o superior
- Librerías:
  - `pandas`
  - `openpyxl` (para leer `.xlsx`)

Instalación recomendada:

```bash
pip install pandas openpyxl
