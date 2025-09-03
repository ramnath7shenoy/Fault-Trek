import time

def memory_stress(duration, intensity=1):
    print(f"[Memory] Allocating memory for {duration}s with intensity {intensity}...")
    big_list = []
    end = time.time() + duration
    while time.time() < end:
        big_list.extend([0] * 10000 * intensity)
    print("[Memory] Done.")
