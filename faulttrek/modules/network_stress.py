import time
import requests

def network_delay(url, duration):
    print(f"[Network] Sending request to {url} with simulated delay {duration}s...")
    time.sleep(duration)
    try:
        response = requests.get(url)
        return response.status_code
    except Exception as e:
        print(f"[Network] Error: {e}")
        return None
