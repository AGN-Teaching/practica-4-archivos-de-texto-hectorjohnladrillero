# Archivos de entrada
nombre_archivo = input("Nombre del archivo de texto a analizar: ")
archivo_diccionario = "palabras.txt"

# Leer palabras correctas (diccionario)
with open(archivo_diccionario, "r", encoding="utf-8") as f:
    contenido_diccionario = f.read()
    palabras_correctas = set(contenido_diccionario.lower().split())

# Leer el texto original
with open(archivo_texto, "r", encoding="utf-8") as f:
    contenido_texto = f.read()
    palabras_texto = contenido_texto.lower().split()

# Detectar palabras mal escritas (no están en el diccionario)
mal_escritas = []
for palabra in palabras_texto:
    # Limpiar signos de puntuación básicos
    palabra_limpia = ''.join(char for char in palabra if char.isalnum())
    if palabra_limpia and palabra_limpia not in palabras_correctas:
        mal_escritas.append(palabra)

# Mostrar resultado
if mal_escritas:
    print("Palabras posiblemente mal escritas:")
    for palabra in mal_escritas:
        print(f"- {palabra}")
else:
    print("No se encontraron errores ortográficos.")
