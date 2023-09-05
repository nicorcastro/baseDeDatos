import pandas as pd

# Ruta del archivo Excel
ruta_archivo_excel = r'C:\Users\NICOR\Desktop\compartirApartamento\programacionOrientada\baseDeDatos\datosBase.xlsx'

# Nombre de la hoja
nombre_hoja = 'hoja1'

# Cargar los datos desde el archivo Excel en un DataFrame
df = pd.read_excel(ruta_archivo_excel, sheet_name=nombre_hoja)

# Ruta del archivo de texto donde se escribirán los datos
ruta_archivo_txt = r'C:\Users\NICOR\Desktop\compartirApartamento\programacionOrientada\baseDeDatos\datos.txt'

# Guardar los datos en un archivo de texto
with open(ruta_archivo_txt, 'w') as archivo:
    for columna in df.columns:
        archivo.write("\n".join(map(str, df[columna].tolist())) + "\n")

# Calcular el promedio, varianza y mediana desde el archivo de texto
with open(ruta_archivo_txt, 'r') as archivo:
    lineas = archivo.readlines()

datos = [float(line.strip()) for line in lineas]
promedio = sum(datos) / len(datos)
varianza = sum((x - promedio) ** 2 for x in datos) / len(datos)
mediana = sorted(datos)[len(datos) // 2]

# Imprimir los resultados
print("Promedio:", promedio)
print("Varianza:", varianza)
print("Mediana:", mediana)
