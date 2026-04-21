$php = New-Object psobject -Property @{
    phpFile = "E:\tech\scripts\php\" + $args[0]
    phpExe = "c:\xampp\php\php.exe"
}
#New-Variable -Name "search_string" -Value "testing"
$phpArg = '"{0}"' -f $php.phpFile
$phpOut = & $php.phpExe -f $phpArg -- $args[1]
$phpOut #> out.txt
#Write-Host $php.phpExe -f $php.phpFile
#Write-Host $phpArg




