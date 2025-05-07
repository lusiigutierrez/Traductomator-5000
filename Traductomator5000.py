"""
----------------------
| Traductomator 5000 |
----------------------
Desarrollado por: Lucía Gutiérrez Cano

"""

import csv
import os
import re
import time
from deep_translator import GoogleTranslator 
from bs4 import BeautifulSoup
from tqdm import tqdm
 
# Diccionario de idiomas
idiomas = {
    "Spanish": "es",
    "English": "en",
    "German": "de",
    "French": "fr",
    "Japanese": "ja",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese": "zh-CN"
}
 
# Ruta del directorio actual
directorio_actual = os.path.dirname(os.path.realpath(__file__))
 
 
# Función para traducir texto (mantiene estructura HTML si la hay)
def traducir_texto(texto, idioma_destino):
    try:
        # Detectar y guardar DOCTYPE si lo hay
        doctype_match = re.match(r'^(<!DOCTYPE html>)(.*)', texto, re.DOTALL)
        doctype = doctype_match.group(1) if doctype_match else ""
        contenido = doctype_match.group(2) if doctype_match else texto
 
        # Reemplazar comillas dobles temporales
        contenido = contenido.replace('""', '{{COMILLA}}')
 
        if "<html" in contenido:
            soup = BeautifulSoup(contenido, 'html.parser')
            for elemento in soup.find_all(string=True):
                if elemento.strip():
                    try:
                        texto_traducido = GoogleTranslator(source='auto', target=idioma_destino).translate(elemento)
                        elemento.replace_with(texto_traducido.replace('{{COMILLA}}', '""'))

                    except Exception as error:
                        print(f"Error al traducir HTML: {error}")

            return doctype + str(soup)
        
        else:
            texto_traducido = GoogleTranslator(source='auto', target=idioma_destino).translate(contenido)
            return doctype + texto_traducido.replace('{{COMILLA}}', '""')
 
    except Exception as error:
        print(f"Error al traducir texto: {error}")
        return texto  # Devuelve el original si falla
 
# Función para procesar cada archivo CSV
def procesar_archivo(nombre_archivo):
    print(f"\nTraduciendo: {nombre_archivo}")
    try:
        ruta_archivo = os.path.join(directorio_actual, nombre_archivo)
 
        with open(ruta_archivo, 'r', encoding='utf-8-sig') as archivo:
            lector = list(csv.reader(archivo, quotechar='"'))
 
        if len(lector) < 2:
            print(f"{nombre_archivo} no tiene suficientes filas.")
            return
 
        idioma_nombre = nombre_archivo.split('_')[1].split('.')[0]
        idioma_destino = idiomas.get(idioma_nombre)
 
        if not idioma_destino:
            print(f"Idioma '{idioma_nombre}' no reconocido.")
            return
 
        print(f"Idioma destino es: {idioma_destino}")
        total_filas = len(lector) - 1
 
        with tqdm(total=total_filas, desc=f"Traduciendo {nombre_archivo}", unit="fila") as barra:
            for fila in lector[1:]:
                time.sleep(0.1)  # para evitar bloqueos por límite de peticiones
                try:
                    fila[3] = traducir_texto(fila[2], idioma_destino)
                    
                except Exception as error:
                    print(f"Error al traducir una fila: {error}")
                    fila[3] = fila[2]
                barra.update(1)
 
        with open(ruta_archivo, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo, quoting=csv.QUOTE_ALL, quotechar='"')
            escritor.writerows(lector)
 
        print(f"Archivo -> {nombre_archivo} terminado")
 
    except Exception as error:
        print(f"Error al procesar el archivo {nombre_archivo}: {error}")
 
# Función principal
def main():
    archivos_csv = [f for f in os.listdir(directorio_actual) if f.endswith('.csv')]

    if not archivos_csv:
        print("No se encontraron archivos .csv en el directorio.")
    else:
        print(f"Archivos encontrados: {archivos_csv}")
        for archivo in archivos_csv:
            procesar_archivo(archivo)

# Solo ejecutar si este archivo es el principal
if __name__ == "__main__":
    main()
 