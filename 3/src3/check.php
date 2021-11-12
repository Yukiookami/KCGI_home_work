<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>check M21W0292</title>
</head>
<body>
<?php
  $userList = array(
    array("userID" => "u1", "password" => "pass1"),
    array("userID" => "u2", "password" => "pass2"),
    array("userID" => "u3", "password" => "pass3")
  );

  $successFlag = false;

  $user = $_POST["userID"];
  $password = $_POST["password"];

  for($i = 0; $i < count($userList); $i++) {
    if ($user === $userList[$i]['userID'] && $password === $userList[$i]['password']) {
      $successFlag = true;
      break;
    }
  }

  if ($successFlag) {
    header("Location: success.html");
  } else {
    header("Location: failure.html");
  }
?>
</body>
</html>
