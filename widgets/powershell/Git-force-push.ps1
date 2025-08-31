<# 
Aggressive Git force-push (PowerShell)
Examples:
  .\Git-force-push.ps1 --branch main --remote origin --retries 3
  .\Git-force-push.ps1 --no-scan
#>

[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ArgsRest = @()   # ensure array, even when no args are passed
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# ---------------- Defaults ----------------
[int]$MAX_RETRIES = 3
[int]$RETRY_DELAY = 5
[string]$BRANCH = 'main'
[string]$REMOTE = 'origin'
[string]$UUID_FILE = Join-Path $env:TEMP '_git_push_uuid.txt'
[bool]$SCAN_TOKENS = $true

# ---------------- Argument Parsing ----------------
function Parse-Args {
    param([string[]]$A = @())
    for ($i = 0; $i -lt $A.Count; $i++) {
        switch -Regex ($A[$i]) {
            '^--branch$'   { $i++; if ($i -lt $A.Count) { $script:BRANCH = $A[$i] }; continue }
            '^--remote$'   { $i++; if ($i -lt $A.Count) { $script:REMOTE = $A[$i] }; continue }
            '^--no-scan$'  { $script:SCAN_TOKENS = $false; continue }
            '^--retries$'  { $i++; if ($i -lt $A.Count) { $script:MAX_RETRIES = [int]$A[$i] }; continue }
            default        { Write-Host "[WARN] Unknown argument: $($A[$i])" }
        }
    }
}
Parse-Args -A $ArgsRest

Write-Host "[INFO] Starting aggressive git force-push script…"
Write-Host "[INFO] Refreshing working state…"

# ---------------- Helpers ----------------
function Test-Command {
    param([Parameter(Mandatory)][string]$Name)
    try { [bool](Get-Command -Name $Name -ErrorAction Stop) } catch { $false }
}

function Refresh-Shell {
    param([string]$ParamFromCaller)
    Write-Host "[INFO] Refreshing shell environment…"
    if (Test-Command 'm') { try { & m back --c *> $null } catch {} }
    if (Test-Command 'b') {
        try {
            if ([string]::IsNullOrWhiteSpace($ParamFromCaller)) {
                & b w --c *> $null
            } else {
                & b $ParamFromCaller --c *> $null
            }
        } catch {}
    }
}

function New-UUID {
    try { ([guid]::NewGuid().ToString()) } catch {
        "$('force-' + (Get-Random -Max 100000000) + (Get-Random -Max 100000000))"
    }
}

function Try-Git {
    param([Parameter(Mandatory)][string]$CmdLine)
    & cmd /c $CmdLine *> $null
    ($LASTEXITCODE -eq 0)
}

function Check-Secrets {
    if (-not $SCAN_TOKENS) { return $true }
    Write-Host "[INFO] Scanning for potential secrets in staged changes…"
    $diff = & git diff --cached 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[WARN] Could not obtain staged diff; skipping secret scan."
        return $true
    }
    $patterns = @(
        'ghp_[A-Za-z0-9][A-Za-z0-9]*',
        'gho_[A-Za-z0-9][A-Za-z0-9]*',
        'ghu_[A-Za-z0-9][A-Za-z0-9]*',
        'ghs_[A-Za-z0-9][A-Za-z0-9]*',
        'ghr_[A-Za-z0-9][A-Za-z0-9]*'
    )
    foreach ($p in $patterns) {
        if ($diff | Select-String -Pattern $p -Quiet) {
            Write-Host "[ERROR] Potential GitHub token detected in staged changes! Aborting."
            return $false
        }
    }
    $true
}

function Force-Push {
    param(
        [Parameter(Mandatory)][string]$Remote,
        [Parameter(Mandatory)][string]$Branch,
        [Parameter(Mandatory)][int]$MaxRetries,
        [Parameter(Mandatory)][int]$RetryDelay
    )
    $attempt = 0
    $success = $false

    while (-not $success -and $attempt -lt $MaxRetries) {
        $attempt++
        Write-Host "[INFO] Force push attempt $attempt of $MaxRetries…"
        if (Try-Git "git push --force-with-lease $Remote $Branch") { $success = $true; break }
        if (Try-Git "git push --force $Remote $Branch")             { $success = $true; break }
        if (-not $success -and $attempt -lt $MaxRetries) {
            Write-Host "[WARN] Push failed, retrying in $RetryDelay seconds…"
            Start-Sleep -Seconds $RetryDelay
        }
    }

    if (-not $success) {
        Write-Host "[WARN] Standard push methods failed, trying nuclear option…"
        Try-Git "git push --delete $Remote $Branch" | Out-Null
        Start-Sleep -Seconds 2
        if (Try-Git "git push -u $Remote $Branch") { $success = $true }
    }
    $success
}

# ---------------- Main ----------------
$callerFirst = if ($ArgsRest.Count -gt 0) { $ArgsRest[0] } else { $null }

try {
    Refresh-Shell -ParamFromCaller $callerFirst

    # Verify repo
    & git rev-parse --is-inside-work-tree *> $null
    if ($LASTEXITCODE -ne 0) { throw "[ERROR] Not a git repository." }

    # Ensure branch
    if (-not (Try-Git "git checkout $BRANCH")) {
        Write-Host "[INFO] Creating branch $BRANCH"
        if (-not (Try-Git "git checkout -b $BRANCH")) {
            throw "[ERROR] Failed to create branch $BRANCH"
        }
    }

    # Stage
    Write-Host "[INFO] Staging all changes…"
    & git add --all *> $null

    # Detect staged changes
    & git diff --cached --quiet *> $null
    $hasChanges = ($LASTEXITCODE -ne 0)

    if ($hasChanges) {
        Write-Host "[INFO] Changes detected, proceeding with commit."
        if (-not (Check-Secrets)) { throw "[ERROR] Secret scan failed." }
        $uuid = New-UUID
        $commitMsg = "Force push: $uuid"
        if (-not (Try-Git "git commit -m `"$commitMsg`"")) {
            throw "[ERROR] Commit failed."
        }
    } else {
        Write-Host "[INFO] No changes to commit, creating empty commit to ensure push."
        Try-Git "git commit --allow-empty -m `"Empty commit to maintain branch`"" | Out-Null
    }

    # Push
    if (-not (Force-Push -Remote $REMOTE -Branch $BRANCH -MaxRetries $MAX_RETRIES -RetryDelay $RETRY_DELAY)) {
        throw "[ERROR] All push attempts failed."
    }

    Write-Host "[SUCCESS] Force push completed successfully!"
}
finally {
    if (Test-Path -LiteralPath $UUID_FILE) {
        try { Remove-Item -LiteralPath $UUID_FILE -Force -ErrorAction SilentlyContinue } catch {}
    }
    Refresh-Shell -ParamFromCaller $callerFirst
    Write-Host "[DONE] Script execution complete."
}
