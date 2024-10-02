def contar_palabras(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as file:  # Abrimos el archivo
            texto = file.read()  # Leemos el contenido del archivo
            palabras = texto.split()  # Separamos el texto en palabras
            
            total_palabras = len(palabras)  # Contamos el total de palabras
            palabras_unicas = set(palabras)  # Usamos un set para obtener palabras únicas
            total_palabras_unicas = len(palabras_unicas)  # Contamos las palabras únicas

            print(f"Total de palabras: {total_palabras}")  # Mostramos el total de palabras
            print(f"Total de palabras no repetidas: {total_palabras_unicas}")  # Mostramos las palabras únicas
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encontró.")  # Manejo de errores si el archivo no existe
    except Exception as e:
        print(f"Ocurrió un error: {e}")  # Manejo de otros errores

# Llamamos a la función
contar_palabras('texto.txt')
