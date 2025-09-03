import os
import argparse
import yaml
from modules.cpu_stress import cpu_stress
from modules.memory_stress import memory_stress
from modules.network_stress import network_delay
from modules.kill_process import kill_process

FAULT_MODULES = {
    "cpu": cpu_stress,
    "memory": memory_stress,
    "network": network_delay,
    "kill": kill_process
}

def run_profile(profile_file):
    print(f"[DEBUG] Current working directory: {os.getcwd()}")
    print(f"[DEBUG] Using profile file: {profile_file}")

    if not os.path.exists(profile_file):
        print(f"[ERROR] Profile file {profile_file} does not exist!")
        return

    with open(profile_file) as f:
        profile = yaml.safe_load(f)

    fault = profile['experiment']['fault']
    target = profile['experiment'].get('target', 'local')
    duration = profile['experiment'].get('duration', 5)

    print(f"[FaultTrek] Injecting {fault} fault into {target} for {duration}s...")

    if fault in FAULT_MODULES:
        if fault == "network":
            print(f"[DEBUG] Starting network fault simulation...")
            status = FAULT_MODULES[fault](target, duration)
            print(f"[FaultTrek] Network request returned status: {status}")
        elif fault == "kill":
            print(f"[DEBUG] Starting process kill simulation...")
            msg = FAULT_MODULES[fault](target)
            print(f"[FaultTrek] {msg}")
        else:
            print(f"[DEBUG] Starting {fault} stress for {duration}s...")
            FAULT_MODULES[fault](duration)
            print(f"[FaultTrek] {fault.capitalize()} stress completed.")
    else:
        print(f"[ERROR] Fault type '{fault}' not recognized.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FaultTrek Chaos Toolkit")
    parser.add_argument("profile", help="YAML file defining the chaos experiment")
    args = parser.parse_args()
    run_profile(args.profile)
    print("[FaultTrek] Experiment finished successfully!")
