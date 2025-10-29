from openai import OpenAI
from dotenv import load_dotenv
import os

# Configuración de la API Key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Base de datos interna (simulación)
historial = {
    "juan pérez - toyota yaris 2018": "Cambio de aceite (01/02/2025), Pastillas de freno (15/03/2025)",
    "maría lópez - nissan versa 2020": "Revisión general (20/02/2025)"
}

tarifas = {
    "cambio de pastillas de freno": "45.000 CLP",
    "cambio de aceite": "25.000 CLP",
    "revisión general": "30.000 CLP"
}

# Función para responder consultas
def asistente_reparaya(pregunta):
    pregunta_lower = pregunta.lower()
    contexto = ""

    # Buscar en el historial de clientes
    for cliente, historial in historial.items():
        if cliente in pregunta_lower:
            contexto += f"Historial de {cliente}: {datos}\n"

    # Buscar tarifas de servicios
    for servicio, precio in tarifas.items():
        if servicio in pregunta_lower:
            contexto += f"Tarifa {servicio}: {precio}\n"

    if not contexto:
        contexto = "No encontré información interna relevante."

    # Llamada a GPT-4o
    response = client.chat.completions.create(
        model="gpt-4o-mini",   # ⚠️ Usa "gpt-4o" si tienes acceso completo
        messages=[
            {"role": "system", "content": "Eres un asistente del taller mecánico ReparaYA. usa solo los datos del contexto."},
            {"role": "user", "content": f"Contexto:\n{contexto}\n\nPregunta del cliente:\n{pregunta}"}
        ],
        max_tokens=200
    )
def obtener_respuesta(response):
    try:
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("Error al comunicarse con OpenAI:", e)
        return "Lo siento, hubo un error al procesar tu solicitud."

# Ejemplo de uso
if __name__ == "__main__":
    preguntas = [
        "¿Cuál es el historial de reparaciones de Juan Pérez - Toyota Yaris 2018?",
        "¿Cuánto cuesta un cambio de pastillas de freno?",
        "¿Puedo agendar una cita para el lunes a las 10:00 hrs?"
    ]

    print("🤖 Asistente ReparaYA\n")
    for p in preguntas:
        print(f"❓ {p}")
        print("✅", asistente_reparaya(p))
        print("-" * 50)
