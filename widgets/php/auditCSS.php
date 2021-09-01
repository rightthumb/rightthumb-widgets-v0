<?php
/*
auditCSS D:\_Scott\S_Documents\Sites\Ny_Pizza\wp-content\themes\storefront\style.css
809,content
the above line is incorrect *** check it out ***
*/
if ( isset($_SERVER['one']) && isset($_SERVER['two']) ) {
	if (is_numeric($_SERVER['one'])) {
		$action = $_SERVER['one'];
		$filename = $_SERVER['two'];
	} else {
		$filename = $_SERVER['one'];
		$action = $_SERVER['two'];
	}
	$do = true;
} else {
	$do = false;
}



//////////////////////////////////////////////////////////// //////////////////////////////////////////////////////////// 
	function getCleanInlineComment($string) {
		$string=str_replace("\r", "", "$string");
		$stringArray = explode("\n",$string);
		foreach ($stringArray as $key => $item) {
	 		if (substr_count($item, "//") > 0) {
				$itemArray = explode("//",$item);
				if (strlen($itemArray[0]) > 0) {
					$stringArray[$key] = $itemArray[0];
				} else {
					$stringArray[$key] = "";
				}
			}
		}
		$string = implode("\r\n",$stringArray);
		return $string;
	}

	function getCleanComment($string) {
		if (substr_count($string, "/*") > 0) {
			for ($x = 0; $x <= substr_count($string, "/*"); $x++) {
				$posStart = strstr($string, '/*');
				$posEnd = strpos($posStart, '*/');
				$item = substr($posStart, 0, $posEnd);
				$item =  $item . "*/";
				$string=str_replace($item, "", $string);
			}
		}
		return $string;
	}

	function getClean($string) {
		for ($x = 0; $x <= 100; $x++)
			$string=str_replace("  ", " ", "[|[$string]|]");

		$string=str_replace("[|[ ", "", "$string");
		$string=str_replace("[|[", "", "$string");
		$string=str_replace(" ]|]", "", "$string");
		$string=str_replace("]|]", "", "$string");
		$string=str_replace("\t", "", "$string");
		$string=str_replace("\r", "", "$string");
		$string=str_replace("\n", "", "$string");

		return $string;
	}

	function getIndividual($string) {
		$string=str_replace(".", " .", "$string");
		$string=str_replace("#", " #", "$string");
		$string=str_replace(">", " ", "$string");
		$string=str_replace("+", "", "$string");
		$string=getClean($string);
		$out=explode(" ",$string);
		foreach ($out as $key => $item) {
			$item = explode(":",$item);
			$out[$key] = $item[0];
		}
		return $out;
	}

	class cssObj {
	    public function __construct($label,$attributes,$individual){
			$this->label = $label;
			$this->attrib = $attributes;
			$this->indi = $individual;
			$this->groups = [];
			foreach ($attributes as $key => $value) {
				$name=$value['name'];
				$value=$value['value'];
				$this->$name = $value;
			}
	    }
	}

	class cssAttribSegments {
	    public function __construct($segment){
			$this->segment = $segment;
			$this->count = 0;
	    }
	}
	class cssAttributes {
	    public function __construct($attribute){
			$this->attrib = $attribute;
	    }
	}
	class cssAttribGroup {
	    public function __construct($abbreviation,$label,$attributes){
			$this->label = $label;
			$this->attrib = $attributes;
			$this->abbrev = $abbreviation;
			$this->members = [];
	    }
	}


//////////////////////////////////////////////////////////// //////////////////////////////////////////////////////////// 
if ($do) {
	$contents=file_get_contents("$filename");
	for ($x = 0; $x <= 100; $x++) {$contents=getCleanInlineComment($contents);}
	for ($x = 0; $x <= 100; $x++) {$contents=getCleanComment($contents);}
	$contents=getClean($contents);
	$i=0;
	$css = [];
	$attributeGroups = [];
	$responsive = [];

		/*
		$attributeGroups[] = new cssAttribGroup('s','size',array(
				'height',
				'line-height',
				'max-height',
				'min-height',
				'max-width',
				'width',
				'min-width'
			));
		*/

	echo "E:\\tech\scripts\php\auditCSS.php \r\n\r\n";
	foreach(explode("}",$contents) as $line0) {
		$line1 = explode("{",$line0);

		if (strpos(strtolower($line1[0]), '@media') !== false) { 
			$string0 = strtolower($line1[0]);
			$string0=str_replace(" ", "", $string0);
			$string0=str_replace("@media", "", $string0);
			$string0=str_replace("(", "", $string0);
			$string0=str_replace(")", "", $string0);
			$string0=str_replace("{", "", $string0);
			$string0=str_replace("-width", "", $string0);
			$string0=str_replace("onlyscreenand", "", $string0);
			$string0=str_replace("and", " - ", $string0);
			$string0=str_replace(":", ": ", $string0);
			$responsive[] = $string0;
		}

		if (count($line1) === 3) {
			$g1 = 1;
			$g2 = 2;
		} elseif (count($line1) === 2) {
			$g1 = 0;
			$g2 = 1;
		}

		if (count($line1) > 1) {
			$label = $line1[$g1];
			$items = explode(";",$line1[$g2]);

			$attributes = [];
			foreach ($items as $itemSet) {
				$itemsSetComponent = explode(":",$itemSet);
				@$name=$itemsSetComponent[0];
				@$value=$itemsSetComponent[1];
				if (strlen($name) > 1) {
					$attributes[] = array(
						'name' => getClean($name),
						'value' => getClean($value)
					);
				}
			}


			if (strlen($label) > 0 && count($attributes) > 0) {
				$labels = explode(",",$label);
				if (count($labels) > 1) {
					foreach ($labels as $labelItem) {
						if (strlen($labelItem) > 0) {
							$css[] = new cssObj(getClean($labelItem),$attributes,getIndividual($labelItem));
						}
					}
				} else {
					$css[] = new cssObj(getClean($label),$attributes,getIndividual($label));
				}
			}////

		}
		$i++;
	}
	////////////////////////////////////////////////////////////


	////////////////////////////////////////////////////////////
	/**/
	$attributeNames = [];
	$attributeItems = [];
	$attributeSegments = [];
	$attributeIndi = [];
	$attributeIndiClass = [];
	$attributeIndiId = [];
	$attributeIndiHtml = [];
	$attributeReport = [];
	foreach ($css as $key => $item) {
		foreach ($css[$key]->indi as $key2 => $item) {
			if (substr_count($css[$key]->indi[$key2], ".")) {
				$attributeIndi[] = $css[$key]->indi[$key2];
				$attributeIndiClass[] = $css[$key]->indi[$key2];
			} elseif (substr_count($css[$key]->indi[$key2], "#")) {
				$attributeIndi[] = $css[$key]->indi[$key2];
				$attributeIndiId[] = $css[$key]->indi[$key2];
			} else {
				$attributeIndiHtml[] = $css[$key]->indi[$key2];
			}
		}
		foreach ($css[$key]->attrib as $key3 => $item) {
			$attributeNames[] = $css[$key]->attrib[$key3]['name'];
			$attributeItems[] = new cssAttributes($css[$key]->attrib[$key3]['name']);
		}
	}
	foreach (array_unique(explode("-",implode("-",array_unique($attributeNames)))) as $key => $segment) {
		if (strlen($segment) > 1)
			$attributeSegments[] = new cssAttribSegments($segment);
	}

	foreach ($attributeSegments as $key => $segment) {
		$segmentName = $attributeSegments[$key]->segment;
		$i = 0;
		foreach ($attributeItems as $key => $item) {
			$itemName = $attributeItems[$key]->attrib;
			if (substr_count(strtolower($itemName), strtolower($segmentName)) > 0) {
				$i++;
			}
		}
		@$attributeSegments[$key]->count = $i;
		if ($i < 100 && $i > 9) {
			$ii = "0" . $i;
		} elseif ($i < 10) {
			$ii = "00" . $i;
		} else {
			$ii = $i;
		}
		$attributeReport[] = "$ii,$segmentName";
	}
	sort($attributeReport);
	////////////////////////////////////////////////////////////
	/**/
	echo "\r\n\r\n________________________________\r\nCSS Report:\r\n\r\n";

	////////////////////////////////////////////////////////////
	if ($action == 1) {
		echo implode("\r\n",$attributeReport);
		echo "\r\n\r\n_______________\r\nTotals:\r\n";

		echo "\r\n\r\nTotal " . count($css) . " Items";
		echo "\r\nTotal " . count(array_unique($attributeIndiId)) . " IDs ";
		echo "\r\nTotal " . count(array_unique($attributeIndiClass)) . " Classes ";
		echo "\r\nTotal " . count(array_unique($attributeIndi)) . " #IDs & .Classes ";
		echo "\r\nTotal " . count(array_unique($attributeIndiHtml)) . " HTML\r\n";
		echo "\r\nTotal " . count($attributeNames) . " Attrib";
		echo "\r\nTotal " . count(array_unique($attributeNames)) . " Attrib Unique";
		echo "\r\nTotal " . count(array_unique(explode("-",implode("-",array_unique($attributeNames))))) . " Attrib Unique Segments\r\n";
		echo "\r\n________________________________\r\n";


		if (count($responsive)) {
			echo "Responsive:\r\n\r\n";
			echo implode("\r\n", array_unique($responsive));
			echo "\r\n________________________________\r\n\r\n";
		} else {
			echo "\r\n";
		}
	}


	////////////////////////////////////////////////////////////
	if ($action == 2) {
		echo implode("\r\n", array_unique($attributeNames));
	}
	////////////////////////////////////////////////////////////
	if ($action == 3) {
		foreach ($css as $key => $item) {
			foreach ($css[$key]->attrib as $key2 => $item)
				echo $css[$key]->attrib[$key2]['name'] . "\r\n";
		}
	}

	if ($action == 4) {
		echo $contents;
	}
	////////////////////////////////////////////////////////////
	//echo var_dump($css);

	if ($action == 5) {
	foreach ($css as $key => $item) { echo $css[$key]->label . "\r\n"; }
		$out = []; foreach ($css as $key => $item) {
			foreach ($css[$key]->indi as $key2 => $item)
				$out[] = $css[$key]->indi[$key2];
		} foreach (array_unique($out) as $key => $item) { echo $item . "\r\n"; }
	}
	////////////////////////////////////////////////////////////
} else {
	echo "Error: Missing input";
}





// var_dump($attributeSegments);