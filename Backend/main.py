import psutil
import time
import requests
import pymysql


def testing_test_in_test(host, port, user, password, database):
    try:
        # Подключение к базе данных
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        # Создание курсора для выпол��ения SQL-запросов
        with connection.cursor() as cursor:
            # Ваш код тестирования здесь
            # Например, выполнение простого SQL-запроса
            cursor.execute("SELECT * FROM your_table LIMIT 1")
            result = cursor.fetchone()
            print(result)  # Вывод результата

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        # Важно закрывать соединение после использования
        if connection:
            connection.close()

def page_testing():
    host = request.args.get('host')
    port = request.args.get('port')
    user = request.args.get('user')
    password = request.args.get('password')
    database = request.args.get('database')
    print(database)
    testing_test_in_test(host, port, user, password, database)

url = "http://example.com"
disk_io_counters = psutil.disk_io_counters()
network_io_counters = psutil.net_io_counters()

response_times = []

for i in range(10):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    response_times.append(end_time - start_time)

print("Requests per second:", 1 / (sum(response_times) / len(response_times)))
print("Disk read bytes per second:", disk_io_counters.read_bytes / 1024 / 1024, "MB/s")
print("Disk write bytes per second:", disk_io_counters.write_bytes / 1024 / 1024, "MB/s")
print("Network bytes received per second:", network_io_counters.bytes_recv / 1024 / 1024, "MB/s")
print("Network bytes sent per second:", network_io_counters.bytes_sent / 1024 / 1024, "MB/s")
