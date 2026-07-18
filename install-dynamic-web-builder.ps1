[CmdletBinding()]
param(
    [switch]$SkipToolInstall,
    [switch]$Skip21stLogin,
    [switch]$SkipBrowserInstall
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function Require-Command {
    param([Parameter(Mandatory)][string]$Name)

    $command = Get-Command $Name -ErrorAction SilentlyContinue
    if (-not $command) {
        throw "Required command '$Name' was not found in PATH."
    }

    return $command.Source
}

function Get-NodeMajorVersion {
    $versionText = (& node --version).Trim()
    if ($versionText -notmatch '^v(?<major>\d+)') {
        throw "Unable to parse Node.js version: $versionText"
    }

    return [int]$Matches.major
}

$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$SourceSkills = Join-Path $RepoRoot '.claude\skills'
$SourceAgent = Join-Path $RepoRoot '.claude\agents\dynamic-web-builder.md'

$ClaudeHome = Join-Path $HOME '.claude'
$PersonalSkills = Join-Path $ClaudeHome 'skills'
$PersonalAgents = Join-Path $ClaudeHome 'agents'
$PersonalBin = Join-Path $ClaudeHome 'bin'

Write-Host '=== Dynamic Web Builder Installer ===' -ForegroundColor Cyan

Require-Command -Name 'claude' | Out-Null
Require-Command -Name 'node' | Out-Null
Require-Command -Name 'npm' | Out-Null
Require-Command -Name 'git' | Out-Null

$NodeMajor = Get-NodeMajorVersion
if ($NodeMajor -lt 20) {
    throw "Node.js 20 or newer is required. Installed version: $(& node --version)"
}

if (-not (Test-Path $SourceSkills)) {
    throw "Source skills directory was not found: $SourceSkills"
}

if (-not (Test-Path $SourceAgent)) {
    throw "Dynamic web builder agent was not found: $SourceAgent"
}

New-Item -ItemType Directory -Force -Path $PersonalSkills, $PersonalAgents, $PersonalBin | Out-Null

Write-Host 'Installing Claude Code skills...' -ForegroundColor Yellow
Get-ChildItem -Path $SourceSkills -Directory | ForEach-Object {
    $destination = Join-Path $PersonalSkills $_.Name
    Copy-Item -Path $_.FullName -Destination $destination -Recurse -Force
    Write-Host "  installed skill: $($_.Name)"
}

Copy-Item -Path $SourceAgent -Destination (Join-Path $PersonalAgents 'dynamic-web-builder.md') -Force
Write-Host '  installed agent: dynamic-web-builder'

if (-not $SkipToolInstall) {
    Write-Host 'Installing current frontend and browser CLIs...' -ForegroundColor Yellow
    & npm install --global '@21st-dev/cli@1.6.0' '@playwright/cli@latest'
    if ($LASTEXITCODE -ne 0) {
        throw 'npm global tool installation failed.'
    }
}

Require-Command -Name '21st' | Out-Null
Require-Command -Name 'playwright-cli' | Out-Null

if (-not $SkipBrowserInstall) {
    Write-Host 'Installing the Playwright browser runtime...' -ForegroundColor Yellow
    & playwright-cli install-browser
    if ($LASTEXITCODE -ne 0) {
        throw 'Playwright browser installation failed.'
    }
}

$LauncherPs1 = @'
[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [string]$ProjectPath = (Get-Location).Path
)

$ErrorActionPreference = 'Stop'
$resolved = (Resolve-Path $ProjectPath).Path
Set-Location $resolved

if (-not (Test-Path (Join-Path $resolved '.git'))) {
    throw "The selected directory is not a Git repository: $resolved"
}

$projectName = Split-Path $resolved -Leaf
$sessionName = ($projectName -replace '[^A-Za-z0-9_-]', '-').ToLowerInvariant()
$env:PLAYWRIGHT_CLI_SESSION = "dynamic-$sessionName"

Write-Host "Repository: $resolved" -ForegroundColor Cyan
Write-Host 'Claude agent: dynamic-web-builder' -ForegroundColor Cyan
Write-Host 'Inside Claude Code, run:' -ForegroundColor Green
Write-Host '  /build-dynamic-web <describe the complete working page or website>' -ForegroundColor Green
Write-Host ''

& claude --agent dynamic-web-builder
exit $LASTEXITCODE
'@

$LauncherPath = Join-Path $PersonalBin 'dynamic-web.ps1'
Set-Content -Path $LauncherPath -Value $LauncherPs1 -Encoding UTF8

$LauncherCmd = @'
@echo off
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%USERPROFILE%\.claude\bin\dynamic-web.ps1" %*
'@
Set-Content -Path (Join-Path $PersonalBin 'dynamic-web.cmd') -Value $LauncherCmd -Encoding ASCII

$UserPath = [Environment]::GetEnvironmentVariable('Path', 'User')
$PathEntries = @($UserPath -split ';' | Where-Object { $_ })
if ($PathEntries -notcontains $PersonalBin) {
    $NewUserPath = (($PathEntries + $PersonalBin) -join ';')
    [Environment]::SetEnvironmentVariable('Path', $NewUserPath, 'User')
    Write-Host "Added to user PATH: $PersonalBin" -ForegroundColor Yellow
}

if (-not $Skip21stLogin) {
    Write-Host 'Checking 21st.dev authentication...' -ForegroundColor Yellow
    & 21st whoami
    if ($LASTEXITCODE -ne 0) {
        Write-Host 'Opening 21st.dev login...' -ForegroundColor Yellow
        & 21st login
        if ($LASTEXITCODE -ne 0) {
            throw '21st.dev login did not complete successfully.'
        }
    }
}

Write-Host ''
Write-Host '=== Installation verified ===' -ForegroundColor Green
Write-Host "Claude: $(& claude --version)"
Write-Host "Node: $(& node --version)"
Write-Host "21st: $(& 21st --version)"
Write-Host 'Playwright CLI: installed'
Write-Host ''
Write-Host 'Open a new PowerShell window, enter any application repository, and run:' -ForegroundColor Cyan
Write-Host '  dynamic-web' -ForegroundColor White
Write-Host ''
Write-Host 'Then give Claude the command:' -ForegroundColor Cyan
Write-Host '  /build-dynamic-web Build <your complete functional outcome>' -ForegroundColor White
