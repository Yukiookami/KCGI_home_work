<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>check.php</title>
</head>
<body>
<?php
$users = array(
	array("uid" => "u1", "pwd" => "p1"),
	array("uid" => "u2", "pwd" => "p2"),
	array("uid" => "u3", "pwd" => "p3"),
	array("uid" => "u4", "pwd" => "p4")
);
$u = $_POST['uid'];
$p = $_POST['pwd'];
?>
あなたのユーザIDは
<?php
echo($u);
?>
で、パスワードは
<?php
echo($p);
?>
ですね。
<?php
$flag = false;
foreach($users as $user){
	// echo("<h1>{$user['uid']},{$user['pwd']}</h1>");
	if($user['uid']==$u && $user['pwd']==$p){ // $userのuidは$uと、pwdは$pと同じ？
		// ログインできる人が見つかった！
		$flag = true;
	}
}
// foreachの後の$flagの値（true or false）で、
// ログインできるかできないかが分かる。


?>
</body>
</html>