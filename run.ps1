# Start the Evidence Intake Workstation locally (Windows PowerShell).
# Evidence and the registry live under $env:EIW_DATA_DIR
# (default: ~\EvidenceIntakeWorkstation) — never inside this repository.
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

$port = if ($env:EIW_PORT) { $env:EIW_PORT } else { "8741" }

if (-not (Test-Path ".venv")) {
    python -m venv .venv
}
& .\.venv\Scripts\Activate.ps1
pip install -q -r backend\requirements.txt

if (-not (Test-Path "frontend\dist") -and (Get-Command npm -ErrorAction SilentlyContinue)) {
    Write-Host "Building frontend (first run)..."
    Push-Location frontend
    npm install --no-audit --no-fund
    npm run build
    Pop-Location
}

New-Item -ItemType Directory -Force -Path ".run" | Out-Null
Write-Host "Evidence Intake Workstation on http://127.0.0.1:$port"
$proc = Start-Process -PassThru -NoNewWindow python `
    -ArgumentList "-m","uvicorn","--factory","backend.app.main:create_app","--host","127.0.0.1","--port",$port
$proc.Id | Out-File ".run\uvicorn.pid"
Wait-Process -Id $proc.Id
