<?php
	header("Content-type:image/jpg");
	if ($_POST["id"] == 0){
		$fname = "plan.jpg";
	}
	else if ($_POST["id"] == 1){
		$fname = "ad.jpg";
	}
	else if ($_POST["id"] == 2){
		$fname = "plan.jpg";
	}
	else if ($_POST["id"] == 3){
		$fname = "collegefests.jpg";
	}
	else{
		$fname = "ad.jpg";
	}
    $file = fopen($fname,"rb");
    $size = filesize($fname);
    $media = fread($file,$size);
	fclose($file);
    echo $media;
?>
