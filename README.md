# Trabajo-INGENIERIA-DE-SOLUCIONES-CON-INTELIGENCIA-ARTIFICIAL-Caso-ReparaYa-
🤖 ReparaYA – Asistente Inteligente para Taller Mecánico
📋 Descripción General

ReparaYA es un asistente inteligente basado en Inteligencia Artificial (IA) diseñado para mejorar la atención al cliente en talleres mecánicos.
Permite consultar historiales de mantenimiento, tarifas de servicios y disponibilidad, utilizando un modelo GPT-4o integrado mediante la API de OpenAI.

El proyecto fue desarrollado como parte de la Evaluación Parcial N°1 del ramo Ingeniería de Soluciones con IA (Duoc UC), cumpliendo con los indicadores IE1-IE10 de la rúbrica oficial.

🧠 Objetivos del Proyecto

Integrar un agente IA funcional con capacidad de razonamiento contextual.

Utilizar frameworks modernos (LangChain, FAISS, OpenAI SDK).

Implementar un pipeline de recuperación de contexto (RAG).

Ofrecer una experiencia personalizada basada en datos internos del taller.

⚙️ Tecnologías Utilizadas
Tecnología	Uso
Python 3.12	Lenguaje principal
OpenAI API (GPT-4o)	Motor de razonamiento y generación de respuestas
LangChain / FAISS (opcional)	Manejo de memoria y recuperación semántica
dotenv	Carga segura de variables del entorno
GitHub	Control de versiones y documentación
🧩 Estructura del Proyecto
📂 ReparaYA/
 ┣ 📄 asistente_reparaya.py      # Código principal del asistente
 ┣ 📄 requirements.txt           # Dependencias
 ┣ 📄 .env                       # Variable de entorno con tu API Key
 ┣ 📄 ReparaYA - Informe.docx    # Documento técnico
 ┣ 📄 Evaluacion-Parcial-N1.pptx # Presentación
 ┗ 📄 README.md                  # Este archivo

🧾 Configuración e Instalación
1️⃣ Clonar el repositorio
git clone https://github.com/tuusuario/reparaya-ia.git
cd reparaya-ia

2️⃣ Instalar dependencias
pip install -r requirements.txt

3️⃣ Configurar la API Key

Crea un archivo llamado .env con el siguiente contenido:

OPENAI_API_KEY=sk-proj-tu_clave_aqui

🚀 Ejecución

Ejecuta el script principal:

python asistente_reparaya.py


Ejemplo de interacción:

❓ ¿Cuál es el historial de reparaciones de Juan Pérez - Toyota Yaris 2018?
✅ Historial: Cambio de aceite (01/02/2025), Pastillas de freno (15/03/2025)

❓ ¿Cuánto cuesta un cambio de pastillas de freno?
✅ Tarifa: 45.000 CLP

🧠 Arquitectura del Agente (Pipeline RAG)
Cliente → Pregunta
   ↓
Módulo de interpretación (GPT-4o / LangChain)
   ↓
Consulta a base de conocimiento interna (FAISS o diccionarios simulados)
   ↓
Recuperación de contexto relevante
   ↓
Generación de respuesta adaptada
   ↓
Entrega al usuario
-----------------------------------------------------------------------------------
📊 Cumplimiento de Indicadores (Rúbrica IE1-IE10)
Indicador	Descripción	Estado
IE1	Configuración de herramientas IA	✅
IE2	Integración de frameworks modernos	✅
IE3	Implementación de memoria contextual	⚙️ Parcial
IE4	Recuperación de contexto semántico	✅
IE5	Planificación de tareas y flujo lógico	✅
IE6	Ejemplo de decisiones adaptativas	✅
IE7	Documentación y diagrama en GitHub	✅
IE8	Justificación de componentes técnicos	✅
IE9	Informe técnico completo	✅
IE10	Lenguaje técnico y coherencia	✅
👥 Autores
Vicente Sanchez

Felipe Caceres

📅 Duoc UC – Ingeniería de Soluciones con IA (EP2_ISY0101)
📍 Octubre 2025
