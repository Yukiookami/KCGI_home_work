<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>test</title>
</head>
<body>
<?php
$now = getdate();

echo("{$now['year']}年{$now['mon']}月{$now['mday']}日");
?>

KCGIには４つのキャンパスがありますが，私は
<?php
	$kcgi = array("百万遍", "京都駅前", "東京", "札幌");
  echo($kcgi[rand(0, 3)]);
?>
キャンパスによく行きます。
</body>

</html>

