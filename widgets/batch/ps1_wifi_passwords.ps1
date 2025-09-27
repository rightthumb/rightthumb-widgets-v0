# Set-ExecutionPolicy Unrestricted -Scope CurrentUser
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass


$profiles = netsh wlan show profiles | Select-String "All User Profile" | ForEach-Object {
    ($_ -split ":")[1].Trim()
}

foreach ($profile in $profiles) {
    $details = netsh wlan show profile name="$profile" key=clear
    $password = $details | Select-String "Key Content" | ForEach-Object {
        ($_ -split ":")[1].Trim()
    }
    if ($password) {
        Write-Host "Profile: $profile - Password: $password"
    } else {
        Write-Host "Profile: $profile - Password: Not Found or Not Set"
    }
}
