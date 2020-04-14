
<script type="text/javascript">
<?PHP


$valet = "Y";
$sStatus ="";


function readCSV($csvFile){
    $file_handle = fopen($csvFile, 'r');
    while (!feof($file_handle) ) {
        $line_of_text[] = fgetcsv($file_handle, 1024);
    }
    fclose($file_handle);
    return $line_of_text;
}


// Set path to CSV file
$csvFile = 'data.csv';

$csv = readCSV($csvFile);
$keys = array_keys($csv);
for ($i=count($csv)-7; $i < count($csv)-1 ; $i++) { 
	# code...
	
		$val = 0;
		if($csv[$i][0] == $valet){
			$val = 2;
		}
		
		if ($val>=2) {
			$sStatus = $sStatus.$csv[$i][1]." : ".$csv[$i][2].";";
		}
	}
echo "parent.update('$sStatus');";
?>
</script>
