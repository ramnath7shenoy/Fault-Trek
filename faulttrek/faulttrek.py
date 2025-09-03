import os
import yaml
import time
import psutil
import threading
import argparse
from flask import Flask, request, jsonify
from prometheus_client import start_http_server, Gauge

# Import fault modules
from modules.cpu_stress import cpu_stress
from modules.memory_stress import memory_stress
from modules.network_stress import network_delay
from modules.kill_process import kill_process

# Flask app
app = Flask(__name__)

# Prometheus metrics
FAULT_STATUS = Gauge("fault_status", "Status of last fault", ["fault_type"])
CPU_USAGE = Gauge("cpu_usage_percent", "CPU usage percent")
MEMORY_USAGE = Gauge("memory_usage_percent", "Memory usage percent")
NETWORK_LATENCY = Gauge("network_latency_ms", "Simulated network latency in ms")

# Fault modules mapping
FAULT_MODULES = {
    "cpu": cpu_stress,
    "memory": memory_stress,
    "network": network_delay,
    "kill": kill_process
}

def collect_system_metrics():
    """Background thread to update Prometheus CPU & RAM usage every second"""
    while True:
        CPU_USAGE.set(psutil.cpu_percent())
        MEMORY_USAGE.set(psutil.virtual_memory().percent)
        time.sleep(1)

def _run_fault(fault, target, duration, intensity):
    """Helper to execute a single fault injection"""
    try:
        if fault not in FAULT_MODULES:
            FAULT_STATUS.labels(fault_type=fault).set(0)
            return f"fault type '{fault}' not recognized"

        if fault == "network":
            print("[DEBUG] Starting network fault simulation...")
            NETWORK_LATENCY.set(duration * 1000)  # simulate latency
            status = FAULT_MODULES[fault](target, duration)
            FAULT_STATUS.labels(fault_type=fault).set(1)
            NETWORK_LATENCY.set(0)
            return f"{fault} fault executed, status={status}"

        elif fault == "kill":
            print("[DEBUG] Starting process kill simulation...")
            msg = FAULT_MODULES[fault](target)
            FAULT_STATUS.labels(fault_type=fault).set(1)
            return msg

        else:  # cpu or memory stress
            print(f"[DEBUG] Starting {fault} stress for {duration}s...")
            FAULT_MODULES[fault](duration, intensity=intensity)
            FAULT_STATUS.labels(fault_type=fault).set(1)
            return f"{fault} stress completed"

    except Exception as e:
        FAULT_STATUS.labels(fault_type=fault).set(0)
        return f"[ERROR] Fault '{fault}' failed: {str(e)}"

def run_profile(profile_file):
    print(f"[INFO] Using profile file: {profile_file}")
    if not os.path.exists(profile_file):
        print(f"[ERROR] Profile file {profile_file} does not exist!")
        return {"status": f"profile {profile_file} not found"}

    with open(profile_file) as f:
        profile = yaml.safe_load(f)

    results = []

    if "experiments" in profile:
        for exp in profile["experiments"]:
            fault = exp["fault"]
            target = exp.get("target", "local")
            duration = exp.get("duration", 10)
            intensity = exp.get("intensity", 1)
            print(f"[INFO] Injecting {fault} fault into {target} for {duration}s (intensity={intensity})")
            results.append(_run_fault(fault, target, duration, intensity))

    elif "experiment" in profile:
        exp = profile["experiment"]
        fault = exp["fault"]
        target = exp.get("target", "local")
        duration = exp.get("duration", 10)
        intensity = exp.get("intensity", 1)
        print(f"[INFO] Injecting {fault} fault into {target} for {duration}s (intensity={intensity})")
        results.append(_run_fault(fault, target, duration, intensity))

    else:
        print("[ERROR] Profile must contain either 'experiment' or 'experiments'")
        return {"status": "invalid profile format"}

    return {"status": "all experiments completed", "results": results}

# HTTP API endpoint to run experiments
@app.route("/run", methods=["POST"])
def run_experiment():
    data = request.get_json()
    profile_file = data.get("profile")
    result = run_profile(profile_file)
    return jsonify(result)

# Health check endpoint for Kubernetes liveness/readiness probes
@app.route("/healthz", methods=["GET"])
def health_check():
    return "OK", 200

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FaultTrek Chaos Toolkit with Prometheus")
    parser.add_argument("--profile", help="YAML file defining the chaos experiment")
    parser.add_argument("--http", action="store_true", help="Start HTTP API")
    parser.add_argument("--metrics_port", type=int, default=8000, help="Prometheus metrics port")
    args = parser.parse_args()

    # Start Prometheus metrics in background
    start_http_server(args.metrics_port)
    threading.Thread(target=collect_system_metrics, daemon=True).start()
    print(f"[INFO] Prometheus metrics exposed at :{args.metrics_port}/metrics")

    # Run single profile if given
    if args.profile:
        run_profile(args.profile)

    # Start HTTP API if requested
    if args.http:
        print("[INFO] Starting HTTP API on port 8080...")
        app.run(host="0.0.0.0", port=8080)
