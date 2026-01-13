<# 
Aggressive Git force-push (PowerShell) — no auto-add, with robust repo detection + debug
Examples:
  .\Git-force-push.ps1 --branch main --remote origin --retries 3
  .\Git-force-push.ps1 --no-scan
  .\Git-force-push.ps1 --repo "D:\path\to\repo" --debug
#>

[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ArgsRest = @()
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
[bool]$DEBUG = $false
[string]$REPO_OVERRIDE = ''

# ---------------- Argument Parsing ----------------
function Parse-Args {
    param([string[]]$A = @())
    for ($i = 0; $i -lt $A.Count; $i++) {
        switch -Regex ($A[$i]) {
            '^--branch$'   { $i++; if ($i -lt $A.Count) { $script:BRANCH = $A[$i] }; continue }
            '^--remote$'   { $i++; if ($i -lt $A.Count) { $script:REMOTE = $A[$i] }; continue }
            '^--no-scan$'  { $script:SCAN_TOKENS = $false; continue }
            '^--retries$'  { $i++; if ($i -lt $A.Count) { $script:MAX_RETRIES = [int]$A[$i] }; continue }
            '^--debug$'    { $script:DEBUG = $true; continue }
            '^--repo$'     { $i++; if ($i -lt $A.Count) { $script:REPO_OVERRIDE = $A[$i] }; continue }
            default        { Write-Host "[WARN] Unknown argument: $($A[$i])" }
        }
    }
}
Parse-Args -A $ArgsRest

# ---------------- Helpers ----------------
function Test-Command { param([string]$Name) try { [bool](Get-Command $Name -ErrorAction Stop) } catch { $false } }

function Refresh-Shell {
    param([string]$ParamFromCaller)
    if (Test-Command 'm') { try { & m back --c *> $null } catch {} }
    if (Test-Command 'b') {
        try {
            if ([string]::IsNullOrWhiteSpace($ParamFromCaller)) { & b w --c *> $null } else { & b $ParamFromCaller --c *> $null }
        } catch {}
    }
}

function New-UUID { try { ([guid]::NewGuid().ToString()) } catch { "force-$((Get-Random -Max 100000000))" } }

function Resolve-RepoRoot {
    param([string]$StartPath)

    # 0) If git can tell us the toplevel from here, prefer it
    $probe = Run-GitC -Repo $StartPath -Args @('rev-parse','--show-toplevel') -Capture
    if ($probe.Code -eq 0 -and $probe.Out) {
        $top = ($probe.Out | Select-Object -First 1).Trim()
        if (Test-Path -LiteralPath $top) { return (Resolve-Path $top).Path }
    }

    # 1) Otherwise walk upward for a valid .git marker
    $gitMarker = Find-GitMarkerUp -Start $StartPath
    if (-not $gitMarker) { return $null }

    $item = Get-Item -LiteralPath $gitMarker -ErrorAction SilentlyContinue
    if ($item -and $item.PSIsContainer) {
        return (Resolve-Path (Split-Path -Parent $gitMarker)).Path
    }

    # .git is a pointer file; working tree is the folder containing the .git file
    return (Resolve-Path (Split-Path -Parent $gitMarker)).Path
}


# Walk upward for .git
# Walk upward for .git (robust: skip invalid pointers, keep walking)
function Find-GitMarkerUp {
    param([string]$Start = (Get-Location).Path)
    $cur = (Resolve-Path $Start).Path
    while ($true) {
        $gitPath = Join-Path $cur ".git"
        if (Test-Path -LiteralPath $gitPath) {
            # Ensure it is actually usable: if it's a pointer, verify target exists
            $item = Get-Item -LiteralPath $gitPath -ErrorAction SilentlyContinue
            if ($null -ne $item) {
                if ($item.PSIsContainer) {
                    return $gitPath
                } else {
                    $gitDir = Resolve-GitDirFromPointer -GitPointerFile $gitPath
                    if ($gitDir -and (Test-Path -LiteralPath $gitDir)) {
                        return $gitPath    # pointer ok; caller will use parent as working tree
                    }
                    # Pointer invalid; keep walking upward instead of returning a bad path
                }
            }
        }
        $parent = Split-Path $cur -Parent
        if ([string]::IsNullOrEmpty($parent) -or ($parent -eq $cur)) { return $null }
        $cur = $parent
    }
}


# If .git is a file, resolve "gitdir: <path>"
function Resolve-GitDirFromPointer {
    param([string]$GitPointerFile)
    try {
        $first = (Get-Content -LiteralPath $GitPointerFile -TotalCount 1)
        if ($first -match '^\s*gitdir:\s*(.+?)\s*$') {
            $p = $Matches[1]
            if (-not [System.IO.Path]::IsPathRooted($p)) {
                $base = Split-Path -Parent $GitPointerFile
                $p = Resolve-Path (Join-Path $base $p)
            } else {
                $p = Resolve-Path $p
            }
            return $p
        }
    } catch {}
    return $null
}

function Debug-Print {
    param([string]$Msg)
    if ($DEBUG) { Write-Host "[DEBUG] $Msg" }
}

function Run-GitC {
    param(
        [Parameter(Mandatory)][string]$Repo,
        [Parameter(Mandatory)][string[]]$Args,
        [switch]$Capture
    )
    Debug-Print "git -C `"$Repo`" $($Args -join ' ')"
    if ($Capture) {
        $out = & git -C "$Repo" @Args 2>&1
        $code = $LASTEXITCODE
        if ($DEBUG) { Write-Host "[DEBUG] exit=$code"; if ($out) { Write-Host "[DEBUG] output:`n$out" } }
        return @{ Code = $code; Out = $out }
    } else {
        & git -C "$Repo" @Args *> $null
        $code = $LASTEXITCODE
        Debug-Print "exit=$code"
        return $code
    }
}

function Try-GitC { param([string]$Repo,[string[]]$Args) ((Run-GitC -Repo $Repo -Args $Args).Equals(0)) }

function Check-SecretsC {
    param([string]$Repo)
    if (-not $SCAN_TOKENS) { return $true }
    $res = Run-GitC -Repo $Repo -Args @('diff','--cached') -Capture
    if ($res.Code -ne 0) { Write-Host "[WARN] Secret scan skipped (no diff)."; return $true }
    $patterns = @('ghp_[A-Za-z0-9]+','gho_[A-Za-z0-9]+','ghu_[A-Za-z0-9]+','ghs_[A-Za-z0-9]+','ghr_[A-Za-z0-9]+')
    foreach ($p in $patterns) {
        if ($res.Out | Select-String -Pattern $p -Quiet) {
            Write-Host "[ERROR] Potential GitHub token detected! Aborting."
            return $false
        }
    }
    $true
}

function Force-PushC {
    param([string]$Repo,[string]$Remote,[string]$Branch,[int]$MaxRetries,[int]$RetryDelay)
    $attempt = 0; $success = $false
    while (-not $success -and $attempt -lt $MaxRetries) {
        $attempt++
        Write-Host "[INFO] Force push attempt $attempt of $MaxRetries…"
        if ((Run-GitC $Repo @('push','--force-with-lease',$Remote,$Branch)) -eq 0) { $success = $true; break }
        if ((Run-GitC $Repo @('push','--force',$Remote,$Branch)) -eq 0)             { $success = $true; break }
        if (-not $success -and $attempt -lt $MaxRetries) { Start-Sleep -Seconds $RetryDelay }
    }
    if (-not $success) {
        Write-Host "[WARN] Trying nuclear option…"
        Run-GitC $Repo @('push','--delete',$Remote,$Branch) | Out-Null
        Start-Sleep -Seconds 2
        if ((Run-GitC $Repo @('push','-u',$Remote,$Branch)) -eq 0) { $success = $true }
    }
    $success
}

# ---------------- Main ----------------
$callerFirst = if ($ArgsRest.Count -gt 0) { $ArgsRest[0] } else { $null }

try {
    if (-not (Test-Command 'git')) { throw "[ERROR] Git is not on PATH." }
    Refresh-Shell -ParamFromCaller $callerFirst



# 1) Determine candidate repo root
$RepoRoot = $null
if ($REPO_OVERRIDE) {
    $RepoRoot = (Resolve-Path $REPO_OVERRIDE).Path
    Debug-Print "REPO_OVERRIDE -> $RepoRoot"
} else {
    $RepoRoot = Resolve-RepoRoot -StartPath (Get-Location).Path
    if (-not $RepoRoot) {
        throw "[ERROR] No git repo detected from $(Get-Location). Use --repo <path> or run inside a repo."
    }
}

# 2) Verify repo with multiple probes and show diagnostics in debug
$isTree     = (Run-GitC -Repo $RepoRoot -Args @('rev-parse','--is-inside-work-tree') -Capture)
$gitDirShow = (Run-GitC -Repo $RepoRoot -Args @('rev-parse','--git-dir') -Capture)
$top        = (Run-GitC -Repo $RepoRoot -Args @('rev-parse','--show-toplevel') -Capture)

if ($DEBUG) {
    Write-Host "----- REPO DIAGNOSTICS -----"
    Write-Host "pwd:            $((Get-Location).Path)"
    Write-Host "RepoRoot:       $RepoRoot"
    Write-Host "--is-inside:    code=$($isTree.Code) out=$($isTree.Out)"
    Write-Host "--git-dir:      code=$($gitDirShow.Code) out=$($gitDirShow.Out)"
    Write-Host "--show-toplevel:code=$($top.Code) out=$($top.Out)"
    Write-Host "----------------------------"
}

# If show-toplevel succeeded, prefer that as canonical root
if ($top.Code -eq 0 -and $top.Out) {
    $maybeTop = ($top.Out | Select-Object -First 1).Trim()
    if (Test-Path -LiteralPath $maybeTop) {
        $RepoRoot = (Resolve-Path $maybeTop).Path
        Debug-Print "Adjusted RepoRoot from --show-toplevel -> $RepoRoot"
    }
}

# Re-check final
$finalTree = (Run-GitC -Repo $RepoRoot -Args @('rev-parse','--is-inside-work-tree') -Capture)
if ($finalTree.Code -ne 0 -or -not ($finalTree.Out -match 'true')) {
    Write-Host "[ERROR] Git did not confirm this as a work tree."
    Write-Host "[HINT] Use --repo <path> to force the repo root or run with --debug to see details."
    throw "[ERROR] Not a git repository."
}





    # # 1) Determine candidate repo root
    # $RepoRoot = $null
    # if ($REPO_OVERRIDE) {
    #     $RepoRoot = (Resolve-Path $REPO_OVERRIDE).Path
    #     Debug-Print "REPO_OVERRIDE -> $RepoRoot"
    # } else {
    #     $gitMarker = Find-GitMarkerUp
    #     if (-not $gitMarker) { throw "[ERROR] No .git found in this folder or any parent." }
    #     if ((Get-Item $gitMarker).PSIsContainer) {
    #         $RepoRoot = Split-Path -Parent $gitMarker
    #         Debug-Print ".git directory at: $gitMarker ; RepoRoot=$RepoRoot"
    #     } else {
    #         $gitDir = Resolve-GitDirFromPointer -GitPointerFile $gitMarker
    #         if (-not $gitDir) {
    #             throw "[ERROR] Found .git file but could not resolve its gitdir pointer."
    #         }
    #         # When .git is a pointer, the working tree is the folder that contains the pointer file
    #         $RepoRoot = Split-Path -Parent $gitMarker
    #         Debug-Print ".git file -> gitdir: $gitDir ; RepoRoot=$RepoRoot"
    #     }
    # }

    # # 2) Verify repo with multiple probes and show diagnostics in debug
    # $isTree = (Run-GitC -Repo $RepoRoot -Args @('rev-parse','--is-inside-work-tree') -Capture)
    # $gitDirShow = (Run-GitC -Repo $RepoRoot -Args @('rev-parse','--git-dir') -Capture)
    # $top = (Run-GitC -Repo $RepoRoot -Args @('rev-parse','--show-toplevel') -Capture)

    # if ($DEBUG) {
    #     Write-Host "----- REPO DIAGNOSTICS -----"
    #     Write-Host "pwd:            $((Get-Location).Path)"
    #     Write-Host "RepoRoot:       $RepoRoot"
    #     Write-Host "--is-inside:    code=$($isTree.Code) out=$($isTree.Out)"
    #     Write-Host "--git-dir:      code=$($gitDirShow.Code) out=$($gitDirShow.Out)"
    #     Write-Host "--show-toplevel:code=$($top.Code) out=$($top.Out)"
    #     Write-Host "----------------------------"
    # }

    # # If show-toplevel succeeded, prefer that as canonical root (fixes nested/alias cases)
    # if ($top.Code -eq 0 -and $top.Out) {
    #     $maybeTop = ($top.Out | Select-Object -First 1).Trim()
    #     if (Test-Path $maybeTop) { $RepoRoot = (Resolve-Path $maybeTop).Path; Debug-Print "Adjusted RepoRoot from --show-toplevel -> $RepoRoot" }
    # }

    # # Re-check final
    # $finalTree = (Run-GitC -Repo $RepoRoot -Args @('rev-parse','--is-inside-work-tree') -Capture)
    # if ($finalTree.Code -ne 0 -or -not ($finalTree.Out -match 'true')) {
    #     Write-Host "[ERROR] Git did not confirm this as a work tree."
    #     Write-Host "[HINT] Use --repo <path> to force the repo root or run with --debug to see details."
    #     throw "[ERROR] Not a git repository."
    # }

    # 3) Ensure branch (no add here)
    if ((Run-GitC -Repo $RepoRoot -Args @('checkout',$BRANCH)) -ne 0) {
        Write-Host "[INFO] Creating branch $BRANCH"
        if ((Run-GitC -Repo $RepoRoot -Args @('checkout','-b',$BRANCH)) -ne 0) {
            throw "[ERROR] Failed to create branch $BRANCH"
        }
    }

    # 4) Detect staged changes
    $quiet = Run-GitC -Repo $RepoRoot -Args @('diff','--cached','--quiet')
    $hasChanges = ($quiet -ne 0)

    if ($hasChanges) {
        if (-not (Check-SecretsC -Repo $RepoRoot)) { throw "[ERROR] Secret scan failed." }
        $uuid = New-UUID
        if ((Run-GitC -Repo $RepoRoot -Args @('commit','-m',"Force push: $uuid")) -ne 0) {
            throw "[ERROR] Commit failed."
        }
    } else {
        Run-GitC -Repo $RepoRoot -Args @('commit','--allow-empty','-m','Empty commit to maintain branch') | Out-Null
    }

    # 5) Push
    if (-not (Force-PushC -Repo $RepoRoot $REMOTE $BRANCH $MAX_RETRIES $RETRY_DELAY)) {
        throw "[ERROR] All push attempts failed."
    }

    Write-Host "[SUCCESS] Force push completed successfully! (Repo: $RepoRoot, Branch: $BRANCH -> $REMOTE)"
}
finally {
    if (Test-Path -LiteralPath $UUID_FILE) {
        try { Remove-Item -LiteralPath $UUID_FILE -Force -ErrorAction SilentlyContinue } catch {}
    }
    Write-Host "[DONE] Script execution complete."
}
