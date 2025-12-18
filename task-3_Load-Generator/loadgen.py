import os
import time
import requests
from statistics import mean

# Read config from environment variables
TARGET = os.getenv("TARGET", "http://javabenchmark-service.default.svc.cluster.local:8080/primecheck")
FREQUENCY = float(os.getenv("FREQUENCY", "2"))  # requests per second

if FREQUENCY <= 0:
    print("FREQUENCY must be > 0, defaulting to 1 req/s")
    FREQUENCY = 1.0

INTERVAL = 1.0 / FREQUENCY  # seconds between requests

response_times = []  # list of successful response times (ms)
failures = 0         # total number of failed requests
total_requests = 0   # total requests sent

print("=== Load Generator Started ===")
print(f"Target   : {TARGET}")
print(f"Frequency: {FREQUENCY} requests/second")
print("Each request will timeout after 10 seconds.")
print("----------------------------------------")

while True:
    start = time.time()
    total_requests += 1

    try:
        # Send HTTP GET request with 10s timeout
        r = requests.get(TARGET, timeout=10)

        if r.status_code == 200:
            elapsed_ms = (time.time() - start) * 1000
            response_times.append(elapsed_ms)
            print(f"[OK]  #{total_requests}  {elapsed_ms:.2f} ms")
        else:
            failures += 1
            print(f"[ERR] #{total_requests}  HTTP {r.status_code}")
    except Exception as e:
        failures += 1
        print(f"[ERR] #{total_requests}  Timeout or exception: {e}")

    # Every 10 requests, print summary
    if total_requests % 10 == 0 and response_times:
        avg_all = mean(response_times)
        avg_last_10 = mean(response_times[-10:])
        print("----- Summary -----")
        print(f"Total requests   : {total_requests}")
        print(f"Total failures   : {failures}")
        print(f"Avg response (all): {avg_all:.2f} ms")
        print(f"Avg response (last 10): {avg_last_10:.2f} ms")
        print("-------------------")

    # Wait so that we respect the frequency (req/s)
    time.sleep(INTERVAL)

