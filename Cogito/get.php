<script>

<?php

$day1 = $_GET["day1"];
$day2 = $_GET["day2"];

$handle = fopen("data.csv", "a");
$v = "";
$good = array("happy","good","amazing","great","impressed","impressive","friendly","appreciate","grateful","thanks","thank","sincere","helpful","best","generous","kind","wonderful","excellent","committment","excellence","innovative","laurels","adoration","delight","delightful");
$bad = array("disappointed","sad","not","bad","poor","better","bugs","average","improve","unhappy","disdain","disappointment","displeasure","dsifavor","dissatisfaction","satisfactory","incomprehension","noncomprehension");

foreach($good as $word1) {

    
    
    if (substr_count($day2, $word1)>0) {
        $v = "Y";
       
    } 
}
if(empty($v)){

	foreach($bad as $word2) {
    
    if (substr_count($day2, $word2)>0) {
        $v = "N";
        
    } 

    if(empty($v))
    	$v = "N";
}

}

$line = array($v,$day1,$day2);
fputcsv($handle, $line);
fclose($handle);
$sStatus = "success;";
echo "parent.update('$sStatus');";

?>

</script>	

