<# 
.SYNOPSIS
  Folder report: recursive size + counts per immediate child of a folder, with
  comma-formatted numbers for readability and numeric Raw fields for CSV sorting.

.EXAMPLE
  .\Get-FolderReport.ps1 -Path "D:\Data"

.EXAMPLE
  .\Get-FolderReport.ps1 -Path "C:\Projects" -OutCsv ".\report.csv" -IncludeHidden

.PARAMETER Path
  Folder to analyze.

.PARAMETER OutCsv
  Optional path to write CSV output.

.PARAMETER IncludeHidden
  Include hidden/system items in the report.

.PARAMETER IncludeFiles
  Also include immediate files (not just subfolders) as rows.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)]
    [ValidateScript({ Test-Path $_ -PathType Container })]
    [string]$Path,

    [string]$OutCsv,

    [switch]$IncludeHidden,

    [switch]$IncludeFiles
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Convert-Size {
    param([long]$Bytes)
    if ($Bytes -lt 1024) { return ("{0:N0} B" -f $Bytes) }
    $units = 'KB','MB','GB','TB','PB'
    $val = [double]$Bytes
    for ($i=0; $i -lt $units.Count; $i++) {
        $val = $val / 1024
        if ($val -lt 1024 -or $i -eq $units.Count-1) {
            return ('{0:N2} {1}' -f $val, $units[$i])
        }
    }
}

function Is-ReparsePoint {
    param([System.IO.FileSystemInfo]$Item)
    return ($Item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0
}

# Normalize root path
$root = (Resolve-Path -LiteralPath $Path).ProviderPath
$force = [bool]$IncludeHidden

Write-Verbose "Root: $root"
Write-Verbose "IncludeHidden: $IncludeHidden  IncludeFiles: $IncludeFiles"

# Collect immediate children (we'll report per these)
$childParams = @{
    LiteralPath = $root
    Force       = $force
    ErrorAction = 'SilentlyContinue'
}
$immediateChildren = Get-ChildItem @childParams | Where-Object {
    $IncludeFiles -or $_.PsIsContainer
}

# Build a one-pass inventory of the tree to avoid N×recurse work
$allFiles = New-Object System.Collections.Generic.List[System.IO.FileInfo]
$allDirs  = New-Object System.Collections.Generic.List[System.IO.DirectoryInfo]

Write-Verbose "Indexing tree (skipping reparse points)…"

# Custom traversal to skip reparse points safely
$stack = [System.Collections.Generic.Stack[System.IO.DirectoryInfo]]::new()
$stack.Push([System.IO.DirectoryInfo]::new($root))

while ($stack.Count -gt 0) {
    $dir = $stack.Pop()

    if (Is-ReparsePoint -Item $dir) { continue }

    if ($dir.FullName -ne $root) { $allDirs.Add($dir) }

    try {
        $items = Get-ChildItem -LiteralPath $dir.FullName -Force:$force -ErrorAction SilentlyContinue
    } catch { continue }

    foreach ($it in $items) {
        if (Is-ReparsePoint -Item $it) { continue }
        if ($it.PSIsContainer) {
            $stack.Push([System.IO.DirectoryInfo]$it)
        } else {
            $allFiles.Add([System.IO.FileInfo]$it)
        }
    }
}

# Map: top-level child path -> files/dirs beneath it
$sep = [IO.Path]::DirectorySeparatorChar
$childMap = @{}
foreach ($child in $immediateChildren) {
    $childMap[$child.FullName] = @{
        Files = New-Object System.Collections.Generic.List[System.IO.FileInfo]
        Dirs  = New-Object System.Collections.Generic.List[System.IO.DirectoryInfo]
        Item  = $child
    }
}

function Get-TopChildPath {
    param([string]$FullPath)
    $prefix = if ($root.EndsWith("$sep")) { $root } else { "$root$sep" }
    if (-not $FullPath.StartsWith($prefix, [System.StringComparison]::OrdinalIgnoreCase)) {
        return $null
    }
    $rel = $FullPath.Substring($prefix.Length)
    $firstSeg = $rel.Split($sep,2)[0]
    return (Join-Path $root $firstSeg)
}

foreach ($f in $allFiles) {
    $top = Get-TopChildPath -FullPath $f.FullName
    if ($null -ne $top -and $childMap.ContainsKey($top)) {
        $childMap[$top].Files.Add($f) | Out-Null
    }
}
foreach ($d in $allDirs) {
    $top = Get-TopChildPath -FullPath $d.FullName
    if ($null -ne $top -and $childMap.ContainsKey($top)) {
        $childMap[$top].Dirs.Add($d) | Out-Null
    }
}

# Build report rows
$rows = New-Object System.Collections.Generic.List[psobject]

foreach ($childPath in $childMap.Keys) {
    $bundle = $childMap[$childPath]
    $child  = $bundle.Item

    if ($child.PSIsContainer) {
        $fileCount = [int64]$bundle.Files.Count
        $dirCount  = [int64]$bundle.Dirs.Count
        $sizeBytes = 0L
        foreach ($f in $bundle.Files) { $sizeBytes += $f.Length }

        $rows.Add([pscustomobject]@{
            Name          = $child.Name
            Type          = 'Directory'
            FullPath      = $child.FullName
            SizeBytes     = ('{0:N0}' -f $sizeBytes)   # formatted with commas
            SizeBytesRaw  = $sizeBytes                 # numeric for CSV sorting
            SizeHuman     = Convert-Size $sizeBytes
            FileCount     = ('{0:N0}' -f $fileCount)   # formatted with commas
            FileCountRaw  = $fileCount
            DirCount      = ('{0:N0}' -f $dirCount)    # formatted with commas
            DirCountRaw   = $dirCount
            LastWrite     = $child.LastWriteTime
            Created       = $child.CreationTime
        }) | Out-Null
    }
    elseif ($IncludeFiles) {
        $rows.Add([pscustomobject]@{
            Name          = $child.Name
            Type          = 'File'
            FullPath      = $child.FullName
            SizeBytes     = ('{0:N0}' -f [int64]$child.Length)
            SizeBytesRaw  = [int64]$child.Length
            SizeHuman     = Convert-Size $child.Length
            FileCount     = ('{0:N0}' -f 1)
            FileCountRaw  = 1
            DirCount      = ('{0:N0}' -f 0)
            DirCountRaw   = 0
            LastWrite     = $child.LastWriteTime
            Created       = $child.CreationTime
        }) | Out-Null
    }
}

# Add a total row for the root
$rootSize = ($allFiles | Measure-Object -Property Length -Sum).Sum
$rows.Add([pscustomobject]@{
    Name          = '[TOTAL]'
    Type          = 'Summary'
    FullPath      = $root
    SizeBytes     = ('{0:N0}' -f $rootSize)
    SizeBytesRaw  = [int64]$rootSize
    SizeHuman     = Convert-Size $rootSize
    FileCount     = ('{0:N0}' -f $allFiles.Count)
    FileCountRaw  = [int64]$allFiles.Count
    DirCount      = ('{0:N0}' -f $allDirs.Count)
    DirCountRaw   = [int64]$allDirs.Count
    LastWrite     = (Get-Item -LiteralPath $root).LastWriteTime
    Created       = (Get-Item -LiteralPath $root).CreationTime
}) | Out-Null

# Output
$sorted = $rows | Sort-Object Type, Name

if ($OutCsv) {
    $sorted | Export-Csv -NoTypeInformation -Encoding UTF8 -Path $OutCsv
    Write-Host "Report written to $OutCsv"
} else {
    # Console table now includes FullPath; -Wrap helps long paths show fully
    $sorted | Format-Table -AutoSize `
        Name, Type, FullPath, SizeHuman, SizeBytes, FileCount, DirCount, LastWrite -Wrap
}
