    # Retrieve all properties of all disk drives
    $drives = Get-WmiObject Win32_DiskDrive | Select-Object *

    # Convert the drives information to JSON
    $jsonOutput = $drives | ConvertTo-Json -Depth 10

    # Output the JSON string
    Write-Output $jsonOutput