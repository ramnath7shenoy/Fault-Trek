import time

def memory_stress(duration=5):
    print(f"[Memory] Allocating memory for {duration}s...")
    mem = [0] * 10**6  # ~4MB allocation
    time.sleep(duration)
    del mem
    print("[Memory] Done.")
