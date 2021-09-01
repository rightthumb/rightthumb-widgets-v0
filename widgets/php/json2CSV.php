<?PHP
$s=$_SERVER['file'];


if (isset($_SERVER['last_field_name'])) {
	$file = file_get_contents("$s");
	$json = str_replace('\n', '', $file);
	$arr = json_decode($json,true);
	array_keys_recursive($arr, $_SERVER['last_field_name']);
}

function array_keys_recursive($myArray, $last_field_return, $MAXDEPTH = INF, $depth = 0, $arrayKeys = array()){
   if($depth < $MAXDEPTH){
        $depth++;
        $keys = array_keys($myArray);
        foreach($keys as $key){
        	if (!is_array($myArray[$key])) {
        		if ($myArray[$key] === 'undefined') {
        			echo '""';
        		} else {
        			echo '"' . formatData($myArray[$key]) . '"';
        		}
        	}

        	if ($key === $last_field_return) {
        		echo "\r\n";
        	} else if (!is_array($myArray[$key])){
        		echo ',';
        	}

            if(is_array($myArray[$key])){
                $arrayKeys[$key] = array_keys_recursive($myArray[$key], $last_field_return, $MAXDEPTH, $depth);
            }
        }
    }

    return $arrayKeys;
}

function formatData($string) {
	$phoneTestResult = false;
	$done = false;
	$phoneTestData = $string;

	$phoneTestData = str_replace(' ', '', $phoneTestData);
	$phoneTestData = str_replace('-', '', $phoneTestData);
	$phoneTestData = str_replace('(', '', $phoneTestData);
	$phoneTestData = str_replace(')', '', $phoneTestData);

	if (is_numeric($phoneTestData) && strlen($phoneTestData) === 10)
		$phoneTestResult = true;

	if ($phoneTestResult) {
		$string = '(' . substr($phoneTestData,0,3) . ') '. substr($phoneTestData,3,3) . '-' . substr($phoneTestData,6,4);
		$done = true;
	}

	if (!$done) {
		$string = str_replace('  ', ' ', $string);
		$string = str_replace('“', "'", $string);
		$string = str_replace('”', "'", $string);
	}




	return $string;
}

?>