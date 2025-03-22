import openpyxl

# PARTE 1: 

estudiantes = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    estudiantes[nombre] = nota

# PARTE 2: 

libro = openpyxl.Workbook()
hoja = libro.active

# PARTE 3: 

hoja['A1'] = "Estudiante"
hoja['B1'] = "Clasificación"

# PARTE 4: 

fila = 2
for nombre, nota in estudiantes.items():
    hoja[f'A{fila}'] = nombre
    if nota > 70:
        hoja[f'B{fila}'] = "Bueno"
    else:
        hoja[f'B{fila}'] = "Regular"
    fila += 1

# PARTE 5: 

libro.save("ejercicio3.xlsx")

print("¡Ejercicio 3 guardado en ejercicio3.xlsx!")