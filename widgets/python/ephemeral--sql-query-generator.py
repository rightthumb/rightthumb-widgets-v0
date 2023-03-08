def query_segment(string,command='OR'):
	if not string.strip(): return ''
	while '  ' in string: string=string.rstrip('  ',' ')

	if '"' in string:
		_string=[]
		for i,sg in enumerate(string.split('"')):
			ii=i+1
			if(ii%2==0):
				x='"'+sg+'"'
				ix=string.index(x)
				string=string[0:ix]+sg.replace(' ','_')+string[ix+len(x):]

		string=string.replace('"','')

	if "'" in string:
		_string=[]
		for i,sg in enumerate(string.split("'")):
			ii=i+1
			if(ii%2==0):
				x="'"+sg+"'"
				ix=string.index(x)
				string=string[0:ix]+sg.replace(" ","_")+string[ix+len(x):]

		string=string.replace("'","")
	xx=[]
	for x in string.split(' '): xx.append(' content LIKE "%'+x.replace('_',' ')+'%" ')
	cmd=' '+command.upper()+' '
	return cmd.join( xx )


ORs = 'repair "success rates" achieved'
ANDs = 'references'
NOTs = 'salesforce "washington ave"'
a=query_segment(ANDs,'AND')
o=query_segment(ORs,'OR')
n=query_segment(NOTs,'AND NOT')
q=''
if not a: q=o
else: q=a+' AND ('+o+')'
if not q: q=n
else: q='('+q+' AND NOT '+n+')'
sql = 'SELECT * FROM documents WHERE ' + q
print(sql)

# same thing in php
"""
<?php

function query_segment($string, $command='OR') {
    if (trim($string) === '') {
        return '';
    }

    while (strpos($string, '  ') !== false) {
        $string = rtrim($string, ' ');
    }

    if (strpos($string, '"') !== false) {
        $_string = array();
        $segments = explode('"', $string);
        foreach ($segments as $i => $sg) {
            $ii = $i + 1;
            if ($ii % 2 == 0) {
                $x = '"' . $sg . '"';
                $ix = strpos($string, $x);
                $string = substr_replace($string, str_replace(' ', '_', $sg), $ix, strlen($x));
            }
        }

        $string = str_replace('"', '', $string);
    }

    if (strpos($string, "'") !== false) {
        $_string = array();
        $segments = explode("'", $string);
        foreach ($segments as $i => $sg) {
            $ii = $i + 1;
            if ($ii % 2 == 0) {
                $x = "'" . $sg . "'";
                $ix = strpos($string, $x);
                $string = substr_replace($string, str_replace(' ', '_', $sg), $ix, strlen($x));
            }
        }

        $string = str_replace("'", '', $string);
    }

    $xx = array();
    $words = explode(' ', $string);
    foreach ($words as $x) {
        $xx[] = ' content LIKE "%' . str_replace('_', ' ', $x) . '%" ';
    }

    $cmd = ' ' . strtoupper($command) . ' ';
    return implode($cmd, $xx);
}

$ORs = 'repair "success rates" achieved';
$ANDs = 'references';
$NOTs = 'salesforce "washington ave"';
$a = query_segment($ANDs, 'AND');
$o = query_segment($ORs, 'OR');
$n = query_segment($NOTs, 'AND NOT');
$q = '';
if (!$a) {
    $q = $o;
} else {
    $q = $a . ' AND (' . $o . ')';
}
if (!$q) {
    $q = $n;
} else {
    $q = '(' . $q . ' AND NOT ' . $n . ')';
}
$sql = 'SELECT * FROM documents WHERE ' . $q;
echo $sql;

?>

"""