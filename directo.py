import pandas as pd

# Ruta del archivo Excel
ruta_archivo_excel = r'C:\Users\NICOR\Desktop\compartirApartamento\programacionOrientada\baseDeDatos\datosBase.xlsx'

# Nombre de la hoja
nombre_hoja = 'hoja1'

# Cargar los datos desde el archivo Excel en un DataFrame
df = pd.read_excel(ruta_archivo_excel, sheet_name=nombre_hoja)

# Ruta del archivo CSV donde se escribirán los datos
ruta_archivo_csv = r'C:\Users\NICOR\Desktop\compartirApartamento\programacionOrientada\baseDeDatos\datos.csv'

# Guardar los datos en un archivo CSV
df.to_csv(ruta_archivo_csv, index=False, header=False)

# Calcular el promedio, varianza y mediana desde el archivo CSV
df_csv = pd.read_csv(ruta_archivo_csv, header=None)
promedio = df_csv.stack().mean()
varianza = df_csv.stack().var()
mediana = df_csv.stack().median()

# Imprimir los resultados
print("Promedio:", promedio)
print("Varianza:", varianza)
print("Mediana:", mediana)
