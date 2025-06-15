import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import os

# Rutas
dataset_path = 'emociones.csv'

# Cargar el dataset o crearlo si no existe
if os.path.exists(dataset_path):
    data = pd.read_csv(dataset_path)
else:
    data = pd.DataFrame(columns=['texto', 'emocion'])

# Entrenar el modelo si hay datos
if len(data) > 0:
    model = make_pipeline(CountVectorizer(), MultinomialNB())
    model.fit(data['texto'], data['emocion'])
else:
    model = None

# Diccionario de respuestas según emoción
respuestas_por_emocion = {
    'triste': [
        "Lamento que te sientas así. Estoy aquí para ti.",
        "Recuerda que después de la lluvia siempre sale el sol ☀️.",
        "Está bien sentirse triste a veces. No estás solo/a."
    ],
    'feliz': [
        "¡Qué bueno! Me alegra saber eso 😊.",
        "¡Eso suena genial! Sigue disfrutando el momento.",
        "¡La felicidad es contagiosa! 🎉"
    ],
    'enojado': [
        "Respira profundo... todo va a estar bien.",
        "Entiendo tu molestia. A veces desahogarse ayuda.",
        "Recuerda que puedes canalizar esa energía de forma positiva."
    ],
    'ansioso': [
        "Tómate un momento para respirar y calmarte.",
        "Está bien sentirse nervioso. Todo pasará.",
        "Estás haciendo lo mejor que puedes. Eso es suficiente por ahora."
    ],
    'emocionado': [
        "¡Eso suena emocionante! Cuéntame más.",
        "¡Wow! Me encanta tu energía ✨.",
        "¡Qué emocionante! Disfrútalo al máximo."
    ]
    # Puedes agregar más emociones aquí
}

print("Escribe una frase y la IA responderá según tu emoción. Escribe 'salir' para terminar.\n")

while True:
    frase = input("Tu frase: ").strip()

    if frase.lower() == 'salir':
        print("Adiós 👋")
        break

    if model is not None:
        emocion = model.predict([frase])[0]
        print(f"🤖 Detecté que estás sintiendo: **{emocion}**")

        # Buscar respuesta empática
        respuestas = respuestas_por_emocion.get(emocion, ["No estoy seguro de qué decir, pero estoy contigo."])
        import random
        respuesta = random.choice(respuestas)

        print(f"🤖 Respuesta: {respuesta}\n")
    else:
        print("Aún no hay suficientes datos para detectar emociones.\n")
