import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import os

# Verificamos si ya existe el dataset
dataset_path = 'emociones.csv'
if os.path.exists(dataset_path):
    data = pd.read_csv(dataset_path)
else:
    # Si no existe, creamos uno nuevo vacío
    data = pd.DataFrame(columns=['texto', 'emocion'])

# Entrenamos el modelo (solo si hay datos suficientes)
if len(data) > 0:
    model = make_pipeline(CountVectorizer(), MultinomialNB())
    model.fit(data['texto'], data['emocion'])
else:
    model = None

print("Escribe una frase y la IA intentará detectar la emoción. Escribe 'salir' para terminar.\n")

while True:
    frase = input("Tu frase: ")

    if frase.lower() == 'salir':
        print("Adiós 👋")
        break

    if model is not None:
        emocion_predicha = model.predict([frase])[0]
    else:
        emocion_predicha = "Desconocido (aún no hay datos suficientes)"

    print(f"🤖 La IA cree que la emoción es: **{emocion_predicha}**")

    respuesta = input("¿Está bien? (si / no): ").strip().lower()

    if respuesta == 'si':
        emocion = emocion_predicha
    elif respuesta == 'no':
        emocion = input("¿Cuál era la emoción correcta?: ").strip().lower()
    else:
        print("Respuesta no entendida. No se guardará la frase.")
        continue

    # Agregamos al dataset
    nuevo_dato = pd.DataFrame([[frase, emocion]], columns=['texto', 'emocion'])
    data = pd.concat([data, nuevo_dato], ignore_index=True)
    data.to_csv(dataset_path, index=False)

    # Volvemos a entrenar el modelo con los nuevos datos
    model = make_pipeline(CountVectorizer(), MultinomialNB())
    model.fit(data['texto'], data['emocion'])

    print("✅ Frase aprendida y modelo actualizado.\n")
