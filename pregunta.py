"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    with open('clusters_report.txt', 'r') as file:
        lines = file.readlines()


        # Crear una lista para almacenar los datos
        data = []

        # Procesar cada línea del archivo
        for line in lines:
            line = line.strip()  # Eliminar espacios en blanco al inicio y al final de la línea
            # Saltar las líneas de encabezado y separador
            if line.startswith(('Cluster', '----')):
                continue
            elif line:  # Procesar líneas con datos
                parts = line.split()  # Dividir la línea en partes separadas por espacios
                cluster = parts[0]
                cantidad = parts[1]
                porcentaje = parts[2]
                # Unir las partes restantes de la línea
                palabras_clave = ' '.join(parts[3:])

                # Agregar los valores a la lista de datos
                data.append([cluster, cantidad, porcentaje, palabras_clave])

        # Crear el dataframe de Pandas
        df = pd.DataFrame(data, columns=['cluster', 'cantidad_de_palabras_clave',
                        'porcentaje_de_palabras_clave', 'principales_palabras_clave'])

        # Convertir los nombres de columnas a minúsculas con guiones bajos
        df.columns = df.columns.str.lower().str.replace(' ', '_')

        # Reemplazar espacios adicionales en las palabras clave
        df['principales_palabras_clave'] = df['principales_palabras_clave'].str.replace(
            r"\s{2,}", ", ")

return df
