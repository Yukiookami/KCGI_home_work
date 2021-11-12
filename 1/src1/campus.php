<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
<?php
  $kcgi = array("百万遍", "京都駅前", "東京", "札幌");
  echo("<h1>{$kcgi[2]}</h1>");

  $kcgiL = array("h" => "百万遍", "k" => "京都駅前", "t" => "東京", "s" => "札幌");
  echo("<h1>{$kcgiL["h"]}</h1>")
?>
</body>
</html>
