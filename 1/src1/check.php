<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>check</title>
</head>
<body>
<?php
  $user = $_POST["userID"];
  $password = $_POST["password"];

  echo("あなたのユーザIDは{$user},パスワードは{$password}ですね。")
?>
</body>
</html>
