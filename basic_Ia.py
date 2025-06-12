import datetime

# Lista donde se almacenarán preguntas que la IA no comprende
preguntas_no_entendidas = []


def responder(pregunta):
    pregunta = pregunta.lower()

    if "hola" in pregunta or "buenas" in pregunta:
        return "¡Hola! ¿Cómo estás hoy?"

    elif "nombre" in pregunta:
        return "Soy una IA básica creada por Steve."

    elif "edad" in pregunta:
        return "No tengo edad como los humanos, pero fui creada hace unos minutos."

    elif "hora" in pregunta:
        ahora = datetime.datetime.now().strftime("%H:%M")
        return f"La hora actual es {ahora}."

    elif "clima" in pregunta:
        return "No tengo sensores del clima aún, pero ojalá sea un buen día."

    elif "adiós" in pregunta or "hasta luego" in pregunta:
        return "¡Hasta pronto! Cuídate."

    elif "triste" in pregunta or "deprimido" in pregunta or "mal" in pregunta:
        return "Siento que te sientas así. Recuerda que incluso los días grises tienen un propósito. 🌤️"

    else:
        preguntas_no_entendidas.append(pregunta)
        return "No entiendo esa pregunta aún, pero estoy aprendiendo poco a poco."


# Bucle principal
print("Escribe 'salir' para terminar.")
while True:
    entrada = input("Tú: ")
    if entrada.lower() == "salir":
        print("IA: ¡Hasta luego! Estas son las preguntas que no entendí:")
        for i, pregunta in enumerate(preguntas_no_entendidas, 1):
            print(f"{i}. {pregunta}")
        break

    respuesta = responder(entrada)
    print("IA:", respuesta)
