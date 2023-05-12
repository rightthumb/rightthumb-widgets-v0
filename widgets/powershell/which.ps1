$cmdOutput = (  (Get-Command $args[0]).Path  ) -join "`n"
echo $cmdOutput
