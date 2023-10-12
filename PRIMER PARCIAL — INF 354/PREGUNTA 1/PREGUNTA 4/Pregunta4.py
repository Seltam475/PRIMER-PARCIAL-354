#4. Aplique a su dataset el etiquetado simple y binario.

from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()
data = housing.data


import pandas as pd
import numpy as np

X = housing.data
y = housing.target

feature_names = [
    "Mediana_Ingresos",
    "Mediana_Edad_Casas",
    "Media_Numero_Habitaciones",
    "Media_Numero_Dormitorios",
    "Poblacion",
    "Hogares_Cerca_Oceanos",
    "Latitud",
    "Longitud"
]

# Convertir el conjunto de datos en un DataFrame de pandas
df = pd.DataFrame(data=X, columns=feature_names)
df['Precio_Mediano'] = y  # Agregar la columna de target al DataFrame

# Etiquetado simple: Convierte la variable target en categorías
etiquetas_simple = ['Bajo' if valor <= 2 else 'Alto' for valor in df['Precio_Mediano']]

# Etiquetado binario: Convierte la variable target en 0 o 1
umbral_binario = 2.5  # Puedes ajustar este umbral según tus necesidades
etiquetas_binarias = [1 if valor > umbral_binario else 0 for valor in df['Precio_Mediano']]

# Agregar las etiquetas al DataFrame
df['Etiquetas_Simple'] = etiquetas_simple
df['Etiquetas_Binarias'] = etiquetas_binarias

# Mostrar el DataFrame con las nuevas etiquetas
print(df.head())