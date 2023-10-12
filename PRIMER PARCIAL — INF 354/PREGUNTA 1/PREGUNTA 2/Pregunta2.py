#2. Realice lo mismo del inciso anterior con el uso de numpy y pandas


from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()
data = housing.data

from re import M
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el conjunto de datos Iris de la biblioteca scikit-learn
column_names = housing.feature_names

# Crear un DataFrame de pandas para el análisis
df = pd.DataFrame(data, columns=column_names)

# Calcular la media, moda, cuartiles y percentiles usando pandas
media = df.mean()
moda = df.mode().iloc[0]
cuartiles = df.quantile([0.25, 0.5, 0.75])
percentiles = df.quantile([0.25, 0.5, 0.75])

print("---------------MEDIA")
print(media)
print("---------------MODA")
print(moda)
print("---------------CUARTILES")
print(cuartiles)
print("---------------PERCENTILES")
print(percentiles)






# GRAFICA DE LOS RESULTADOS


fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Gráfico de barras para la media
axes[0, 0].bar(column_names, media)
axes[0, 0].set_title('Media')

# Gráfico de barras para la moda
axes[0, 1].bar(column_names, moda)
axes[0, 1].set_title('Moda')

# Gráfico de cajas para los cuartiles
cuartiles.T.plot(kind='box', ax=axes[1, 0])
axes[1, 0].set_title('Cuartiles')

# Gráfico de cajas para los percentiles
percentiles.T.plot(kind='box', ax=axes[1, 1])
axes[1, 1].set_title('Percentiles')

plt.tight_layout()
plt.show()