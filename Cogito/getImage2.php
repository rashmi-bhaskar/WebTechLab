<?php
	header("Content-type:image/jpg");
	if ($_POST["id"] == 0){
		$fname = "blog.jpg";
	}
	else if ($_POST["id"] == 1){
		$fname = "chat.jpg";
	}
	else if ($_POST["id"] == 2){
		$fname = "pitch.jpg";
	}
	else if ($_POST["id"] == 3){
		$fname = "chat.jpg";
	}
	else{
		$fname = "blog.jpg";
	}
    $file = fopen($fname,"rb");
    $size = filesize($fname);
    $media = fread($file,$size);
	fclose($file);
    echo $media;
?>
