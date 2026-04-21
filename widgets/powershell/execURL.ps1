param (
    [Parameter(Mandatory=$true)]
    [string]$url
)

try {
    # Fetch the content from the given URL
    $scriptContent = Invoke-WebRequest -Uri $url -UseBasicParsing
    # Execute the downloaded script content
    Invoke-Expression $scriptContent.Content
} catch {
    Write-Error "An error occurred: $_"
}

