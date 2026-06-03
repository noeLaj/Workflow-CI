from prometheus_client import start_http_server, Counter, Gauge
import time
import random

REQUEST_COUNT = Counter("request_count", "Total requests")
MODEL_ACCURACY = Gauge("model_accuracy", "Model accuracy")
LATENCY = Gauge("latency", "Model latency")

start_http_server(8000)

while True:
    REQUEST_COUNT.inc()
    MODEL_ACCURACY.set(random.uniform(0.7, 0.85))
    LATENCY.set(random.uniform(0.1, 0.5))
    time.sleep(5)
