function wifi {
    $outputFile = "WiFiPasswords.csv"
    $wifiProfiles = netsh wlan show profiles | Select-String -Pattern "All User Profile" | ForEach-Object {
        $_ -replace '^.*: ', ''
    }

    # Create an empty array to hold the results
    $results = @()

    # Iterate through each profile to fetch its password
    foreach ($profile in $wifiProfiles) {
        $wifiInfo = netsh wlan show profile name="$profile" key=clear | Select-String -Pattern "Key Content"
        $password = if ($wifiInfo) { $wifiInfo.ToString().Split(":")[1].Trim() } else { "No password" }
        $results += [PSCustomObject]@{
            WiFiName = $profile
            Password = $password
        }
    }

    $results | Export-Csv -Path $outputFile -NoTypeInformation

    $results | Format-Table -AutoSize
    Remove-Item -Path $outputFile
}


