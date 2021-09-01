<?PHP
$file=file_get_contents("~ipOwner.txt");
//echo"$file";
$name="";
foreach(explode("\r\n",$file) as $line){

//	$posStart = strstr("$line]", "]");
//	$posEnd = strpos($posStart, ': ');
//	$line = substr($posStart, 0, $posEnd);
	$line=str_replace('[ ', '', "[$line");
	$line=str_replace('[', '', "[$line");
	$line=str_replace('.', '', "$line");
	$line=str_replace(', Inc', '', "$line");
	$line=str_replace('Inc', '', "$line");
	$line=str_replace(', LLC', '', "$line");
	$line=str_replace('LLC', '', "$line");
	$line=str_replace(' ]', '', "$line]");
	$line=str_replace(']', '', "$line");
//	if(strlen($line) > 6) {echo "$line\n";}
	if (strpos($line, '<') !== true && strlen($line) > 6) {
		$name="$name\n$line";
	}
	
}
$name = implode("\n",array_unique(explode("\n", $name)));
echo"$name";
?>