# импорт необходимых библиотек
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score

# предсказанные значения
y_pred = [0, 1, 0, 1, 1]

# реальные значения
y_true = [0, 1, 1, 0, 1]

# вычисление точности
accuracy = accuracy_score(y_true, y_pred)
print("Accuracy:", accuracy)

# вычисление среднеквадратической ошибки
mse = mean_squared_error(y_true, y_pred)
print("MSE:", mse)

# вычисление R-квадрат
r2 = r2_score(y_true, y_pred)
print("R-squared:", r2)

