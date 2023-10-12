from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest, f_regression

# Cargar el conjunto de datos
data = fetch_california_housing()
X = data.data
y = data.target

# Convertir a DataFrame para mayor flexibilidad
df = pd.DataFrame(data=X, columns=data.feature_names)
df['target'] = y

# 1. Manejo de valores faltantes con SimpleImputer
imputer = SimpleImputer(strategy='mean')
df = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# 2. Escalado de características con StandardScaler
scaler = StandardScaler()
df[data.feature_names] = scaler.fit_transform(df[data.feature_names])

# 3. División de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_selected, df['target'], test_size=0.2, random_state=42)

print(data)