<?php
extract($_GET);
$file = fopen("chat.txt","a+");
echo $msg;
fwrite($file,$msg.";");
fclose();
?>
