Get-ChildItem -Path . -Recurse | Where-Object { $_.Attributes -match 'ReparsePoint' } | ForEach-Object {
    if ((Get-Item $_.FullName).Target -eq "D:\.rightthumb-widgets\widgets\bash\vps-bashrc_extended.sh") {
        $_.FullName
    }
}
