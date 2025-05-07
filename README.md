# 🌍 Traductomator 5000

**Traductomator 5000** es una herramienta desarrollada como parte de mi Trabajo de Fin de Grado en Ingeniería Informática. Su objetivo es automatizar la traducción de archivos `.csv`, manteniendo la estructura HTML si existe, y generando archivos listos para su uso en diferentes idiomas. Está especialmente pensada para casos en los que es necesario traducir grandes volúmenes de contenido.

## 📌 Funcionalidad

- Detecta automáticamente el idioma a partir del nombre del archivo.
- Traduce el contenido de los archivos `.csv` utilizando Google Translate.
- Conserva etiquetas HTML como `<html>`, `<body>`, etc., durante la traducción.
- Respeta estructuras y comillas especiales para mantener la integridad del formato.
- Muestra barra de progreso en la terminal mientras se traducen las filas.
- Reescribe el archivo original con el contenido traducido.

## 🚀 Tecnologías utilizadas

- **Python 3.x**
- [deep-translator](https://pypi.org/project/deep-translator/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [tqdm](https://pypi.org/project/tqdm/)

## 💻 Requisitos

Instala las dependencias necesarias ejecutando:
pip install deep-translator beautifulsoup4 tqdm


## ▶️ Cómo usar
Coloca el archivo .csv que quieras traducir en la misma carpeta que el script.

Asegúrate de que el nombre del archivo siga un formato tipo:

nombreArchivo_English.csv
nombreArchivo_Spanish.csv
nombreArchivo_German.csv

Ejecuta el script:
python3 Traductomator5000.py

El archivo se procesará y traducirá automáticamente, reescribiendo el original con el contenido traducido.

## 🧪 Ejemplo de uso
Archivo original:
LevelLayoutSection_Italian.csv con contenido en italiano y código HTML.

Traducción generada:
El archivo LevelLayoutSection_Italian.csv se sobrescribirá con el contenido traducido al italiano, manteniendo el formato y etiquetas HTML si las hay.

Estructura esperada:
Se espera que el contenido a traducir esté en la columna 3 (índice 2) y que la traducción se almacene en la columna 4 (índice 3).

## 🌐 Idiomas soportados
- Español
- Inglés
- Alemán
- Francés
- Japonés
- Italiano
- Portugués
- Ruso
- Chino


## 👩‍💻 Autora
Lucía Gutiérrez Cano
Trabajo de Fin de Grado – Ingeniería Informática

