frases = {
    "Hola": "¡Buenos días!",
    "Adiós": "¡Hasta pronto!",
    "¿Cómo estás?": "Estoy muy bien, ¿y tú?",
}

frase_usuario = input("Escribe una frase: ")

if frase_usuario in frases:
    print(frases[frase_usuario])
else:
    print(f"No conozco la frase '{frase_usuario}'.")
