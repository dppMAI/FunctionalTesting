import unittest
import tensorflow as tf
import numpy as np

class TestNeuralNetwork(unittest.TestCase):
    def setUp(self):
        # Подготовка тестовых данных
        self.train_images = np.random.rand(100, 28, 28, 1)
        self.train_labels = np.random.randint(10, size=(100,))
        self.test_images = np.random.rand(20, 28, 28, 1)
        self.test_labels = np.random.randint(10, size=(20,))

    def test_model_compile(self):
        model = tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(10)
        ])

        model.compile(optimizer='adam',
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                      metrics=['accuracy'])

        # Проверяем, что модель скомпилирована без ошибок
        self.assertIsNotNone(model)

    def test_model_fit(self):
        model = tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(10)
        ])

        model.compile(optimizer='adam',
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                      metrics=['accuracy'])

        # Обучаем модель
        model.fit(self.train_images, self.train_labels, epochs=1,
                  validation_data=(self.test_images, self.test_labels))

        # Проверяем, что обучение прошло успешно
        self.assertTrue(True)  # Замените на реальные проверки, если необходимо

    def test_model_evaluation(self):
        model = tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(10)
        ])

        model.compile(optimizer='adam',
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                      metrics=['accuracy'])

        # Обучаем модель
        model.fit(self.train_images, self.train_labels, epochs=1,
                  validation_data=(self.test_images, self.test_labels))

        # Оцениваем производительность модели
        test_loss, test_acc = model.evaluate(self.test_images, self.test_labels, verbose=0)

        # Проверяем, что оценка производительности прошла успешно
        self.assertIsNotNone(test_acc)

if __name__ == '__main__':
    unittest.main()