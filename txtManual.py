# Ruta del archivo de texto con los datos
ruta_archivo_texto = r'C:\Users\NICOR\Desktop\compartirApartamento\programacionOrientada\baseDeDatos\datos.txt'

# Leer los datos desde el archivo de texto
with open(ruta_archivo_texto, 'r') as archivo:
    lineas = archivo.readlines()

# Convertir las líneas a valores numéricos
datos = [float(linea.strip()) for linea in lineas]

# Calcular el promedio, varianza y mediana
promedio = sum(datos) / len(datos)
varianza = sum((x - promedio) ** 2 for x in datos) / len(datos)
mediana = sorted(datos)[len(datos) // 2]

# Imprimir los resultados
print("Promedio:", promedio)
print("Varianza:", varianza)
print("Mediana:", mediana)
