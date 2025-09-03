#!/bin/bash

profiles=("profiles/cpu.yaml" "profiles/memory.yaml" "profiles/network.yaml" "profiles/crash.yaml" "profiles/latency.yaml")

for profile in "${profiles[@]}"; do
    echo
    echo "============================================="
    echo "Running FaultTrek profile: $profile"
    echo "============================================="
    docker run --rm faulttrek sh -c "python faulttrek.py $profile"
    echo "============================================="
    sleep 2
done
