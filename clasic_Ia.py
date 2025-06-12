# Sistema experto básico para diagnóstico de salud
def diagnosticar():
    print("👩‍⚕️ Bienvenido al sistema de diagnóstico. Responde con 'sí' o 'no'.")

    # Preguntamos por síntomas
    fiebre = input("¿Tienes fiebre? ").lower()
    tos = input("¿Tienes tos? ").lower()
    dolor_garganta = input("¿Te duele la garganta? ").lower()
    dificultad_respirar = input("¿Tienes dificultad para respirar? ").lower()
    dolor_cabeza = input("¿Tienes dolor de cabeza? ").lower()

    # Evaluamos condiciones según respuestas (reglas lógicas)
    if fiebre == "si" and tos == "si" and dificultad_respirar == "si":
        print("🤖 Posible diagnóstico: Podrías tener COVID-19. Consulta a un médico.")

    elif fiebre == "si" and tos == "si" and dolor_garganta == "si":
        print("🤖 Posible diagnóstico: Podrías tener gripe.")

    elif dolor_garganta == "si" and fiebre == "no":
        print("🤖 Posible diagnóstico: Parece un resfriado leve.")

    elif dolor_cabeza == "si" and fiebre == "no" and tos == "no":
        print("🤖 Posible diagnóstico: Puede ser estrés o migraña.")

    else:
        print("🤖 No se pudo determinar un diagnóstico claro. Consulta a un profesional.")


# Ejecutamos el sistema
diagnosticar()
