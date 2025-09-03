#!/bin/bash

# Ensure logs folder exists
mkdir -p logs

# List of profiles to run
profiles=("faulttrek/profiles/cpu.yaml" "faulttrek/profiles/memory.yaml" "faulttrek/profiles/network.yaml" "faulttrek/profiles/crash.yaml" "faulttrek/profiles/latency.yaml")

# Run each profile
for profile in "${profiles[@]}"; do
    echo
    echo "============================================="
    echo "Running FaultTrek profile: $profile"
    echo "============================================="
    
    # Run the profile in Docker and save logs
    docker run --rm -v $(pwd)/logs:/app/logs faulttrek sh -c "python -m faulttrek.faulttrek --profile $profile > logs/$(basename $profile .yaml).log 2>&1"
    
    echo "Logs saved to logs/$(basename $profile .yaml).log"
    echo "============================================="
    sleep 2
done

echo "All profiles executed. Check the logs folder for details."
