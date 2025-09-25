import time
import requests

def network_delay(url, duration=None):
    """
    Measure real network latency when sending a request.
    Optionally simulate additional delay (duration seconds).
    """
    try:
        # Start timer before the request
        start = time.time()
        response = requests.get(url)
        end = time.time()

        # Calculate actual latency
        latency = end - start

        # Optional artificial delay (if duration provided)
        if duration:
            print(f"[Network] Simulating extra delay of {duration}s...")
            time.sleep(duration)

        print(f"[Network] Request to {url} returned {response.status_code} "
              f"in {latency:.3f} seconds (real latency).")

        return {"status_code": response.status_code, "latency": latency}

    except Exception as e:
        print(f"[Network] Error contacting {url}: {e}")
        return None
