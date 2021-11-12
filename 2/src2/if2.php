<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
<h1>if-else文</h1>
<?php

$val = 10;

if($val == 10) {
	echo 'valは10と等しい。(10)<br>';
} else {
	echo 'valは10と等しくない(..,7,8,9,11,12,13...)<br>';
}

if($val > 10) {
	echo 'valは10より大きい(11,12,13,...)<br>';
} else {
	echo 'valは10以下(10,9,8,7,...)<br>';
}

if($val < 10) {
	echo 'valは10より小さい(9,8,7,...)<br>';
} else {
	echo 'valは10以上(10,11,12,13,...)<br>';
}

if($val >= 10) {
	echo 'valは10以上(10,11,12,13,...)<br>';
} else {
	echo 'valは10より小さい(9,8,7,...)<br>';
}

if($val <= 10) {
	echo 'valは10以下(10,9,8,7,...)<br>';
} else {
	echo 'valは10より大きい(11,12,13,...)<br>';
}

if($val != 10) {
	echo 'valは10と等しくない(..,7,8,9,11,12,13...)<br>';
} else {
	echo 'valは10と等しい。(10)<br>';
}

?>
<hr>
elseの部分は ifの条件が成立しないときのみ実行<br>
<br>
else ブロックは書かなくても良い。<br>
if文の条件式を変更すると elseブロックと同等の条件にできる<br>
</body>
</html>
