import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных
data = pd.read_csv('data.csv')

# Определение функции потерь
def loss_function(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

# Определение оптимизатора
from sklearn.linear_model import LinearRegression
optimizer = LinearRegression()

# Разделение данных на обучающую и тестовую выборки
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data[['input_size', 'read_speed', 'write_speed']], data['latency'], test_size=0.2, random_state=42)

# Обучение модели
optimizer.fit(X_train, y_train)

# Предсказание значений на тестовой выборке
y_pred = optimizer.predict(X_test)

# Вычисление функции потерь на тестовой выборке
loss = loss_function(y_test, y_pred)

# Визуализация результатов
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.title('Performance Analysis')
plt.show()

# Вывод результатов
print('Loss: ', loss)
