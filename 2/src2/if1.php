<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
<h1>if文と条件判断</h1>
<?php

$val = 10;

if($val == 10) {
	echo 'valは10と等しい。(10)<br>';
}

if($val > 10) {
	echo 'valは10より大きい(11,12,13,...)<br>';
}

if($val < 10) {
	echo 'valは10より小さい(9,8,7,...)<br>';
}

if($val >= 10) {
	echo 'valは10以上(10,11,12,13,...)<br>';
}

if($val <= 10) {
	echo 'valは10以下(10,9,8,7,...)<br>';
}

if($val != 10) {
	echo 'valは10と等しくない(..,7,8,9,11,12,13...)<br>';
}

?>
<hr>
if(条件式) { 条件式が成立した時のみ，ここの内容を実行 }<br>
条件式が成立しない時は，すぐ後ろの{ }の中を実行しない。<br>

</body>
</html>
