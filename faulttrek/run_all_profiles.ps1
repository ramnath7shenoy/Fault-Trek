$profiles = @(
    "profiles/cpu.yaml",
    "profiles/memory.yaml",
    "profiles/network.yaml",
    "profiles/crash.yaml",
    "profiles/latency.yaml"
)

foreach ($profile in $profiles) {
    Write-Host "`n============================================="
    Write-Host "Running FaultTrek profile: $profile"
    Write-Host "=============================================`n"

    # Use sh -c to force the container to run Python correctly
    docker run --rm faulttrek sh -c "python faulttrek.py $profile"

    Write-Host "`n=============================================`n"
    Start-Sleep -Seconds 2  # small pause between experiments
}
