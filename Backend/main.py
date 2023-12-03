import psutil
import time
import requests

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
