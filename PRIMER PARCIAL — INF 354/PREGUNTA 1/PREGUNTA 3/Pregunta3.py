# 3. Del dataset elegido realice la imputación por columnas sin scikit-learn.

from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()
data = housing.data



import numpy as np

# Encuentra las columnas con valores NaN
col_nan = np.isnan(data).any(axis=0)

# Imputación por columna (usando la media en este caso)
for i in range(data.shape[1]):
    if col_nan[i]:
        # Calcula la media de la columna i
        media_columna = np.nanmean(X[:, i])
        # Encuentra las posiciones con NaN en la columna i
        nan_indices = np.isnan(data[:, i])
        # Reemplaza los NaN con la media de esa columna
        data[nan_indices, i] = media_columna

print(data)
