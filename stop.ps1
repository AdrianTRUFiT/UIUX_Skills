# Stop the Evidence Intake Workstation started by run.ps1.
Set-Location $PSScriptRoot
if (Test-Path ".run\uvicorn.pid") {
    $procId = Get-Content ".run\uvicorn.pid"
    Stop-Process -Id $procId -ErrorAction SilentlyContinue
    Remove-Item ".run\uvicorn.pid"
    Write-Host "stopped"
} else {
    Write-Host "no pid file - nothing to stop"
}
