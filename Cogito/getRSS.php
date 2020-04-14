<?php
    header("Content-type:text/xml");
    $data = file_get_contents("rss.xml");
    echo $data
?>
