$source = $args[0]
$destination = $args[0] + ".zip"

# Write-Host "args[0] " $args[0]
# Write-Host "args[1] " $args[1]
# Write-Host "args[2] " $args[2]

 If(Test-path $destination) {Remove-item $destination}
Add-Type -assembly "system.io.compression.filesystem"
[io.compression.zipfile]::CreateFromDirectory($Source, $destination)