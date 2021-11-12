<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>arrayTest.php</title>
</head>
<body>
配列に対する繰り返し
<?php
$users = array("タナカ", "キムラ", "スズキ");
// for($i=0; $i<=count($users)-1; $i++){
foreach($users as $u){
	echo("<br>あなたはキムラさんですか？");
	if($u == "キムラ"){
		echo("はい。");
		break;
	}else{
		echo("ちがいます。わたしは{$u}です。");
	}
}
?>
</body>
</html>
