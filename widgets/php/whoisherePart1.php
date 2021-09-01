<?PHP
$file=file_get_contents("~whoishere.txt");
$ip="";
foreach(explode("\r\n",$file) as $line){
	$line = substr("$line", -34, 23);
	$line=str_replace(' ', '', $line);
	$posStart = strstr("[$line", "[");
	$posEnd = strpos($posStart, ':');
	$line = substr($posStart, 0, $posEnd);
	$line=str_replace('[', '', $line);
	if (strpos($line, '192.168') !== true  && strlen($line) > 6) {
		$ip="$ip\n$line";
	}
	
}
$ip = implode("\n",array_unique(explode("\n", $ip)));
echo"$ip";
?>