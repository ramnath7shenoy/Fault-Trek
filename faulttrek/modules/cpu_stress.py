import time

def cpu_stress(duration, intensity=1):
    print(f"[CPU] Stressing CPU for {duration}s with intensity {intensity}...")
    end = time.time() + duration
    while time.time() < end:
        sum(i*i for i in range(10000 * intensity))
    print("[CPU] Done.")
