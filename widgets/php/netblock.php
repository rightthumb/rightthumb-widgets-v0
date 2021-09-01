<?php 
$s=$_SERVER['search'];
$s=str_replace(" ", "+", $s);
$url = "http://whois.arin.net/rest/nets;q=$s?showDetails=true&showARIN=false";
//$url = "http://whois.arin.net/rest/net/NET-98-24-0-0-1";

	$page = file_get_contents("$url");

//file_put_contents("netblock.txt", $page);
$i=1;
foreach(explode(".",$s) as $octet){
	if($i < 4) {
		if($i > 1){$network="$network.$octet";}else{$network="$octet";}
		}
	$i++;
	}
$network="$network.0";
	$posStart = strstr($page, "$network");
	$posEnd = strpos($posStart, 'http://whois.arin');
	$output = substr($posStart, 0, $posEnd);
	$output=str_replace("</resources>", "[] ", $output);
	$output=str_replace('<orgRef handle="', '', $output);
	$output=str_replace('" name="', ': ', $output);
	$output=str_replace('">', '.', $output);

if ($output === ""){
	$i=1;$network="";
	foreach(explode(".",$s) as $octet){
	if($i < 3) {
		if($i > 1){$network="$network.$octet";}else{$network="$octet";}
		}
	$i++;
	}
	$network="$network.0.0";//echo"$network\n";
}
	$posStart = strstr($page, "$network");
	$posEnd = strpos($posStart, 'http://whois.arin');
	$output = substr($posStart, 0, $posEnd);
	$output=str_replace("</resources>", "[] ", $output);
	$output=str_replace('<orgRef handle="', '', $output);
	$output=str_replace('" name="', ': ', $output);
	$output=str_replace('">', '.', $output);
if ($output === ""){
	$i=1;$network="";
	foreach(explode(".",$s) as $octet){
	if($i < 2) {
		if($i > 1){$network="$network.$octet";}else{$network="$octet";}
		}
	$i++;
	}
	$network="$network.0.0.0";//echo"$network\n";
}
	$posStart = strstr($page, "$network");
	$posEnd = strpos($posStart, 'http://whois.arin');
	$output = substr($posStart, 0, $posEnd);
	$output=str_replace("</resources>", "[] ", $output);
	$output=str_replace('<orgRef handle="', '', $output);
	$output=str_replace('" name="', ': ', $output);
	$output=str_replace('">', '.', $output);







	
	
	
	
	
	
	
	
	
	
	
/////
	$output=str_replace("$network", "", $output);
	$output=str_replace('</startAddress></netBlock></netBlocks><pocs inaccuracyReportUrl="http://www.arin.net/public/whoisinaccuracy/index.xhtml" termsOfUse="https://www.ari', '', $output);
	$output=str_replace('n.net/whois_tou.html"/><resources inaccuracyReportUrl="http://www.arin.net/public/whoisinaccuracy/index.xhtml" termsOfUse="https://www.arin.net/whois_tou.h', '', $output);
	$output=str_replace('tml<limitExceeded limit="256false</limitExceeded>', '', $output);
/////
//echo"[$output]";
if (strlen($output)< 1){
	$posStart = strstr($page, '<orgRef handle="');
	$posEnd = strpos($posStart, 'http://whois.arin.net');
	$output = substr($posStart, 0, $posEnd);
	$output=str_replace("</resources>", "[] ", $output);
	$output=str_replace('<orgRef handle="', '', $output);
	$output=str_replace('" name="', ': ', $output);
	$output=str_replace('">', '.', $output);
	$output=str_replace('<orgRe f handle="', '', $output);
//	echo "$output";
}

$pos = strpos($output, "[]");
if ($pos !== false) {
	$posStart = strstr($output, "[]");
	$posEnd = strpos($posStart, '.');
	$output = substr($posStart, 0, $posEnd);
	$output=str_replace("[]", "", $output);	
}
if ($output === ""){
	echo"\n";
	echo "$page";
	echo"\n";
} else {
	echo"\n";
	echo "$output";
	echo"\n";	
}
 ?>
