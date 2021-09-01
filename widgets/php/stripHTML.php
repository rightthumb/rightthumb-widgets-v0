<?php
$file=file_get_contents("HTML.htm");
$file=str_replace("’", "'", $file);
$file = mb_convert_encoding($file, "UTF-8");
$file=str_replace("’", "'", $file);
/*
$file=str_replace("<ul", "\n<ul", $file);
$file=str_replace("<li", "\n<li", $file);
$file=str_replace("<p", "\n<p", $file);
$file=str_replace("<div", "\n<div", $file);

$file=str_replace("<UL", "\n<UL", $file);
$file=str_replace("<LI", "\n<LI", $file);
$file=str_replace("<P", "\n<P", $file);
$file=str_replace("<DIV", "\n<DIV", $file);

$file=str_replace("</p>", "</p>\n", $file);
$file=str_replace("</div>", "</div>\n", $file);

$file=str_replace("</P>", "</P>\n", $file);
$file=str_replace("</DIV>", "</DIV>\n", $file);
*/

$file=strip_tags("$file");

$file=str_replace("ÿþ", " ", $file);
$file=str_replace("&nbsp;", " ", $file);
$file=str_replace("\r", "\n", $file);
$file=str_replace("\n ", "\n", $file);
$file=str_replace(" \n", "\n", $file);
$file=str_replace("\n\n", "\n", $file);
$file=str_replace("\n\n", "\n", $file);
$file=str_replace("\n\n", "\n", $file);
$file=str_replace("\n\n", "\n", $file);
$file=str_replace("\n", "\r\n", $file);


$file=str_replace("–", "-", $file);
$file=str_replace("’", "'", $file);
$file=str_replace("&lt;", "<", $file);
$file=str_replace("&gt;", ">", $file);

file_put_contents("HTML.txt", $file);






?>