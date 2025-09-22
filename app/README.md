# Aplicación de la Ingeniería de Prompts

Este directorio contiene la aplicación Python para la optimización del servicio de ecommerce.

## Configuración del Proyecto

Este proyecto utiliza [uv](https://docs.astral.sh/uv/) como gestor de paquetes y entorno virtual de Python.

### Requisitos Previos

- Python 3.8 o superior
- uv instalado en tu sistema

### Comandos de Configuración

#### 1. Inicializar el proyecto

```bash
uv init
```

#### 2. Instalar dependencias

```bash
uv sync
```

#### 3. Agregar dependencias adicionales (ejemplo)

```bash
uv add requests fastapi uvicorn
```

#### 4. Agregar dependencias de desarrollo

```bash
uv add --dev pytest black flake8
```

### Ejecución

#### Ejecutar la aplicación principal

```bash
uv run python main.py
```

#### Ejecutar con un comando específico

```bash
uv run --script start
```

#### Activar el entorno virtual manualmente

```bash
source .venv/bin/activate  # En Linux/Mac
# o
.venv\Scripts\activate     # En Windows
```

### Estructura del Proyecto

```bash
app/
├── README.md
├── pyproject.toml
├── main.py
├── src/
│   └── ...
└── tests/
    └── ...
```

## Github Token

Crear un token de GitHub [aquí](https://github.com/settings/personal-access-tokens/new?description=Used+to+call+GitHub+Models+APIs+to+easily+run+LLMs%3A+https%3A%2F%2Fdocs.github.com%2Fgithub-models%2Fquickstart%23step-2-make-an-api-call&name=GitHub+Models+token&user_models=read)

### Crear variable de entorno con el token de GitHub

#### Bash

```bash
export GITHUB_TOKEN="<your-github-token-goes-here>"
```

#### Powershell

```powershell
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```

#### windows CLI

```cli
set GITHUB_TOKEN=<your-github-token-goes-here>
```
