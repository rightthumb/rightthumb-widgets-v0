
Function Get-Information {
  Write-Host "Starting the gathering of information, be patient, this could take a while!`r`n"
  Write-Host "- Gathering Data`r`n- Returning Data`r`n"

  [PSCustomObject]@{
    "Test1" = "Value1"
    "Test2" = "Value2"
  }

  Write-Host "Information Gathering Complete!"
}

Function Convert-Information {
  Param(
    [Parameter(ValueFromPipeline=$true)]$Param
  )

  $Param | ConvertTo-JSON
}
# Get-Information | Convert-Information
# Write-Output | Convert-Information
ConvertTo-JSON