$profiles = @(
    "faulttrek/profiles/cpu.yaml",
    "faulttrek/profiles/memory.yaml",
    "faulttrek/profiles/network.yaml",
    "faulttrek/profiles/crash.yaml",
    "faulttrek/profiles/latency.yaml"
)

foreach ($profile in $profiles) {
    Write-Host "`n============================================="
    Write-Host "Running FaultTrek profile: $profile"
    Write-Host "=============================================`n"

    # Use sh -c to force the container to run Python module correctly
    docker run --rm faulttrek sh -c "python -m faulttrek.faulttrek $profile"

    Write-Host "`n=============================================`n"
    Start-Sleep -Seconds 2  # small pause between experiments
}
