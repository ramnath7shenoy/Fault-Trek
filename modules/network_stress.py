import time
import requests

def network_delay(target="https://httpbin.org/get", duration=5):
    print(f"[Network] Sending request to {target} with simulated delay {duration}s...")
    time.sleep(duration)
    r = requests.get(target)
    return r.status_code
