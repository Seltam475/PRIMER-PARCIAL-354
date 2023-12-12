#Con PYTHON sin librerías construya los índices de al menos dos ciclos para un Split de Train 80 y test de 20, apliquelo en el dataset iris.

from sklearn.datasets import load_iris
import random

#Cargar el conjunto de datos iris
iris = load_iris()
X = iris.data
y = iris.target

#Definir la proporción de división entre entrenamiento y prueba
split_ratio = 0.8
split_index = int(len(X) * split_ratio)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train = X[:split_index]
y_train = y[:split_index]
X_test = X[split_index:]
y_test = y[split_index:]

#Implementar un modelo simple sin usar bibliotecas externas
def simple_classifier(features):
    #Aqui se quiere lograr clasificar las caracteristicas
    #si es menor a 5, entonces cera clase 0,
    #y si es mayor o igual sera clase 1
    
    if features[0] < 5:
        return 0
    else:
        return 1

# Realizar predicciones en el conjunto de prueba
predictions = [simple_classifier(features) for features in X_test]

# Calcular la precisión del modelo
correct_predictions = sum(1 for true_label, predicted_label in zip(y_test, predictions) if true_label == predicted_label)
accuracy = correct_predictions / len(y_test) * 100

print(f"Precisión del modelo: {accuracy:.2f}%")
