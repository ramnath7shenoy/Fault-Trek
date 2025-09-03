import time

def cpu_stress(duration=5):
    print(f"[CPU] Stressing CPU for {duration}s...")
    end = time.time() + duration
    while time.time() < end:
        pass
    print("[CPU] Done.")
