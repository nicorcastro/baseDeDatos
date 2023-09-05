import pandas as pd

# Ruta y nombre del archivo Excel
ruta_archivo = r'C:\Users\NICOR\Desktop\compartirApartamento\programacionOrientada\baseDeDatos\datosBase.xlsx'
hoja = 'hoja1'  # Reemplaza con el nombre de la hoja donde están los datos

# Leer los datos del archivo Excel
df = pd.read_excel(ruta_archivo, sheet_name=hoja, header=None)

# Calcular la media, el promedio, la varianza y la mediana

# Inicializar variables para acumular la media y el promedio
media_acumulativa = 0
promedio_acumulativo = 0

# Recorrer cada columna para calcular la media y el promedio acumulativos
for columna in df.columns:
    media = df[columna].mean()  # Calcular la media solo para la columna actual
    media_acumulativa += media
    
    # Calcular el promedio para la columna actual sumando todos los valores y dividiendo por la cantidad de filas
    promedio = df[columna].sum() / len(df)
    promedio_acumulativo += promedio

# Calcular los valores finales de media y promedio
media_final = media_acumulativa / len(df.columns)
promedio_final = promedio_acumulativo / len(df.columns)

# Calcular varianza y mediana usando métodos de Pandas
varianza = df.stack().var()
mediana = df.stack().median()

# Mostrar los resultados

# Imprimir la media total calculada
print("Media Total:", media_final)

# Imprimir el promedio calculado
print("Promedio:", promedio_final)

# Imprimir la varianza calculada
print("Varianza:", varianza)

# Imprimir la mediana calculada
print("Mediana:", mediana)

#CODIGO REVISADO Y EDITADO POR SANDRA