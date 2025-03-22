- Esta documentación describe detalladamente el proceso de creación del proyecto, desde la configuración inicial hasta la ejecución del código. 

1. Configuración Inicial del Proyecto

- Creación de la carpeta del proyecto:
Se creó una carpeta llamada clasificacion_notas para organizar todos los archivos del proyecto.

- Inicialización del repositorio Git:
Dentro de la carpeta clasificacion_notas, se ejecutó el comando git init para inicializar un repositorio Git. Esto permitió llevar un control de versiones del código.

- Creación del archivo .gitignore:
Se creó un archivo llamado .gitignore en la raíz del proyecto.
Se agregó la línea venv/ a este archivo para indicar a Git que ignore la carpeta venv, que contiene el entorno virtual.

2. Creación del Entorno Virtual

- Creación del entorno virtual:
Dentro de la carpeta clasificacion_notas, se ejecutó el comando python -m venv venv para crear un entorno virtual llamado venv.

- Activación del entorno virtual:
En Windows, se ejecutó el comando venv\Scripts\activate para activar el entorno virtual.
La activación del entorno virtual asegura que las bibliotecas se instalen y utilicen dentro del contexto del proyecto.

3. Instalación de Dependencias

- Instalación de openpyxl:
Con el entorno virtual activado, se ejecutó el comando pip install openpyxl para instalar la biblioteca openpyxl, que permite trabajar con archivos de Excel.

- Generación del archivo requirements.txt:
Se ejecutó el comando pip freeze > requirements.txt para generar un archivo requirements.txt que contiene una lista de todas las bibliotecas instaladas en el entorno virtual.

4. Desarrollo del Código

- Creación del archivo main.py:
Se creó un archivo llamado main.py en la raíz del proyecto para contener el código Python.

- Implementación del ejercicio:
Se importó la biblioteca openpyxl.
Se creó un diccionario vacío llamado 'estudiantes' para almacenar los nombres de los estudiantes y sus notas.
Se utilizó un bucle for para pedir al usuario los nombres y notas de 3 estudiantes, y se almacenaron en el diccionario estudiantes.
Se creó un nuevo libro de trabajo de Excel utilizando openpyxl.Workbook().
Se obtuvo la hoja de cálculo activa del libro de trabajo utilizando libro.active.
Se escribieron los encabezados "Estudiante" y "Clasificación" en las celdas A1 y B1, respectivamente.
Se utilizó un bucle for para iterar sobre el diccionario estudiantes y escribir los nombres y clasificaciones de los estudiantes en las columnas A y B, respectivamente.
Se utilizó una condicional if nota > 70: para determinar la clasificación de cada estudiante (Bueno o Regular).
Se guardó el libro de trabajo de Excel en un archivo llamado ejercicio3.xlsx utilizando libro.save("ejercicio3.xlsx").
Se imprimió un mensaje de confirmación indicando que el archivo se ha guardado correctamente.
Solución de errores:
El error "NameError: name 'openpyxl' is not defined" se solucionó asegurándose de que la biblioteca openpyxl estuviera instalada en el entorno virtual activo.

5. Ejecución del Código

* Clonar el repositorio en la terminal con https://github.com/sheylaarodelo/Evaluaci-n-desempe-o.git
* Luego debes poner cd al lado del archivo cd clasificacion_notas
* Poner Code . para que se nos abra en Visual.
* Luego en la terminal de Visual crear el entorno: python -m venv venv
* Después activarlo: venv\Scripts\activate.
* Por último ejecuta el proyecto con: python main.py

Se siguieron las instrucciones en la terminal para ingresar los nombres y notas de los estudiantes.
Se generó el archivo ejercicio3.xlsx con los resultados.
