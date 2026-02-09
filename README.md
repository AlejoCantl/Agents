# Agente Bedrock

Agente de IA que se conecta a AWS Bedrock usando el modelo Claude Haiku.

## Qué hace

- `agent.py`: Crea un agente que usa el modelo Claude Haiku de AWS Bedrock
- `session.py`: Maneja la autenticación y conexión con AWS

## Requisitos

```
annotated-types==0.7.0
anyio==4.12.1
attrs==25.4.0
awscrt==0.29.2
boto3==1.42.43
botocore==1.42.43
certifi==2026.1.4
cffi==2.0.0
click==8.3.1
colorama==0.4.6
cryptography==46.0.4
docstring_parser==0.17.0
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
httpx-sse==0.4.3
idna==3.11
importlib_metadata==8.7.1
jmespath==1.1.0
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
mcp==1.26.0
opentelemetry-api==1.39.1
opentelemetry-instrumentation==0.60b1
opentelemetry-instrumentation-threading==0.60b1
opentelemetry-sdk==1.39.1
opentelemetry-semantic-conventions==0.60b1
packaging==26.0
pycparser==3.0
pydantic==2.12.5
pydantic-settings==2.12.0
pydantic_core==2.41.5
PyJWT==2.11.0
python-dateutil==2.9.0.post0
python-dotenv==1.2.1
python-multipart==0.0.22
pywin32==311
referencing==0.37.0
rpds-py==0.30.0
s3transfer==0.16.0
six==1.17.0
sse-starlette==3.2.0
starlette==0.52.1
strands-agents==1.25.0
typing-inspection==0.4.2
typing_extensions==4.15.0
urllib3==2.6.3
uvicorn==0.40.0
watchdog==6.0.0
wrapt==1.17.3
```

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python agent.py
```

## Configuración

Requiere credenciales de AWS configuradas:
- Perfil predeterminado de AWS
- O variables de entorno con `aws_access_key_id` y `aws_secret_access_key`
- O parámetros directos en `session.py`
