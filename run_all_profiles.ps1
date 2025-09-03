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

    docker run --rm faulttrek python faulttrek.py $profile

    Write-Host "`n=============================================`n"
    Start-Sleep -Seconds 2  # small pause between experiments
}
