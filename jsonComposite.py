import json
import os

def merge_json_files(directory, output_file):
    """
    Esta función toma todos los archivos JSON en un directorio especificado y los combina en un único archivo JSON.
    Cada archivo JSON se convierte en un elemento de una lista en el archivo de salida.

    Args:
    directory (str): El camino al directorio que contiene los archivos JSON.
    output_file (str): El nombre del archivo JSON de salida.
    """
    json_list = []
    
    # Recorre todos los archivos en el directorio especificado
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            # Abre y lee el archivo JSON
            with open(file_path, 'r') as file:
                data = json.load(file)
                json_list.append(data)  # Agrega el diccionario al final de la lista
    
    # Escribe la lista de diccionarios en el archivo de salida
    with open(output_file, 'w') as file_out:
        json.dump(json_list, file_out, indent=4)  # Usa indentación para mejor legibilidad

