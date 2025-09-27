    param (
 $days = '90'
)
foreach($process in Get-Process |
 where Path |
 select -Unique) {
 $dir = $process |
 Get-ChildItem;
New-Object -TypeName PSObject -Property @{'Name' = $process.name;
 'Description' = $process.Description;
 'File Version' = $process.FileVersion;
 'Product' = $process.Product;
 'Path' = $process.Path;
 'Modified Date' = $dir.LastWriteTime;} |
 where 'Modified Date' -gt (Get-Date).AddDays(-$days)}