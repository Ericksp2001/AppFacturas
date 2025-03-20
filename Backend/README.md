# API de Procesamiento de Documentos con OCR e IA

## Descripción
Esta API está desarrollada en **Python** utilizando **FastAPI** y proporciona dos servicios principales:

1. **Procesamiento de documentos con OCR**: Permite la recepción de un conjunto de documentos y extrae el contenido de texto de cada uno.
2. **Procesamiento de Texto con IA**: Recibe un texto, lo envía a un modelo de IA para su análisis y genera un archivo Excel con los resultados.

## Requisitos del Sistema
- Python 3.9+

## Instalación
```bash
# Clonar el repositorio
git clone https://github.com/Ericksp2001/fastapi-ocr-ai.git
cd fastapi-ocr-ai

# Crear un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## Ejecución del Servidor
```bash
uvicorn main:app --reload
```

## Endpoints
### 1. Procesamiento de documentos con OCR
**`POST /ocr/process`**
- **Descripción**: Recibe un conjunto de documentos, extrae su contenido y devuelve un JSON con los textos.
- **Entrada**: Archivos PDF.
- **Salida**:
```json
{
    "documents": [
        {"filename": "doc1.pdf", "text": "Contenido del documento 1"},
        {"filename": "doc2.png", "text": "Contenido del documento 2"}
    ]
}
```

### 2. Procesamiento de Texto con IA
**`POST /ai/analyze`**
- **Descripción**: Recibe un JSON con un texto y lo procesa mediante IA.
- **Entrada**:
```json
{
    "text": "Este es un texto de ejemplo para analizar."
}
```
- **Salida**: Un archivo Excel generado con los resultados del análisis.

### 3. Seguridad y Monitoreo
**`GET /health`**
- **Descripción**: Verifica el estado del servidor.
- **Salida**:
```json
{
    "status": "OK"
}
```

## Seguridad
- Eliminación automática de documentos tras su procesamiento.
- Protección contra ataques **DDoS** mediante límites de peticiones y autenticación.

## Tiempos de Respuesta
- El tiempo de respuesta del backend debe ser menor a **20 segundos** por petición.

