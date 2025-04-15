# 🤖 Semana 0 - Backend con FastAPI + IA local (Ollama)

Este proyecto implementa una API básica que permite interactuar con un modelo de inteligencia artificial local (`deepseek-r1`) usando FastAPI y Ollama.

## 🚀 Tecnologías Utilizadas
- **Python** 3.11+
- **FastAPI** - Framework web rápido para APIs
- **Uvicorn** - Servidor ASGI de alto rendimiento
- **Ollama** - Modelo de IA local
- **Postman** - Cliente para pruebas de API
- **dotenv** - Manejo de variables de entorno

## ⚙️ Instalación

1. Clonar el repositorio e instalar dependencias:
```bash
git clone https://github.com/mastero101/semana0_Alejandro_Castro.git
cd semana0-backend-ia
python -m venv env
source env/bin/activate  # o .\env\Scripts\activate en Windows
pip install -r requirements.txt
```

## ▶️ Ejecución

```bash
uvicorn app.main:app --reload
```
🔍 Conceptos Básicos

 ¿Qué es Ollama?
Es una plataforma para correr modelos LLM locales como DeepseekR1, Mistral, Llama3.3 

 ¿Qué es FastAPI?
Framework utilizado para construir rapidamentes y manera sencilla APIs con Python, inclusive generando documentacion como swagger util para pruebas

 ¿Qué es el modelo deepseek-r1?
Modelo de lenguaje preentrenado previamente usando gran potencia de computo y transformers enfocado a generacion de texto en base a preguntas del usuario

 Uso de peticiones con stream=True
Funcion que permite recibir datos en tiempo real de un modelo de IA. En este caso se utiliza para recibir datos de un modelo de IA en tiempo real, similar a socketio o comunicaciones bidireccionales.

  ¿Cómo garantizar la escalabilidad de una API que consume modelos de IA pesados?
Creando colas para las tareas y balanceadores de carga con servidores, contenedores o scripts trabajando en paralelo y direccionando el tráfico a los servidores adecuados.

  ¿Qué parámetros de Ollama (ej: num_ctx, temperature) afectan el rendimiento/calidad?
temperature: Controla la aleatoriedad de la salida del modelo. Un valor más alto (como 0.8) puede generar respuestas más creativas y variadas, mientras que un valor más bajo (como 0.2) puede producir respuestas más deterministas.

top_k: Controla la cantidad de opciones de palabras más probables que el modelo considera en cada paso. Un valor más alto (10) puede generar respuestas más creativas, mientras que un valor más bajo (1) puede producir respuestas más concretas y cuadradas

num_ctx: Controla el tamaño del contexto del modelo. Un valor más alto (2048) puede permitir una mayor capacidad de memoria y contexto, mientras que un valor más bajo (1024) puede reducir la memoria requerida y mejorar el rendimiento. Pero no permitiendo intrudcir un contexto amplio

stop: Permite especificar palabras o frases que, si se encuentran en la salida del modelo, detendrán la generación de texto. Esto puede ser útil para evitar que el modelo genere respuestas largas o no coherentes.

  ¿Qué estrategias usar para balancear carga entre múltiples instancias de Ollama?
Se pueden utilizar balanceadores de carga como nginx para enviar las peticiones a las distintas instancias VM, contenedores o scripts ejecutados en paralelo en un cluster o tener un servicio especializado para el balanceo de carga usando estrategias como round-robin, least-connections, etc.

  ¿Qué patrones de diseño (ej: CQRS, Singleton) son útiles para integrar modelos de IA en backend?
CQRS: Separar lectura/escritura.
Singleton: Compartir modelo en toda la app.
Factory: Crear instancias del modelo por tipo/cliente.
Decorator: Para logging, autenticación, validación extra.

