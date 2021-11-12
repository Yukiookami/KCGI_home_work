<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
<?php
$now = getdate();
echo("{$now['year']}年{$now['mon']}月{$now['mday']}日");
?>
現在、KCGIには４つのキャンパスがありますが、私は
<?php
$r = rand(0, 3);
$kcgi = array(
	"Hyakumanben","KyotoEki","Tokyo","Sapporo");
echo("<h1>{$kcgi[$r]}</h1>");
?>
によく行きます。
<?php
$kcgi = array(
	"h"=>"Hyakumanben", "k"=>"KyotoEki",
	"t"=>"Tokyo", "s"=>"Sapporo");
echo("<h1>{$kcgi['k']}</h1>");
?>
</body>
</html>
