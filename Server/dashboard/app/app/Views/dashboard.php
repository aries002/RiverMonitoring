<div style="text-align:center;">
    <h2 style="font-weight:bold;-webkit-text-stroke: 5px #000000;paint-order:stroke fill;">
        <span style="color:red;">Sungai</span> <span style="color:yellow;">Monitoring</span>
    </h2>
</div>
<?php
$bmkg_tropodo = file_get_contents("https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4=35.15.06.2010");
$area_tropodo = json_decode($bmkg_tropodo);
$cuaca_tropodo = $area_tropodo->data[0]->cuaca[0];
// print_r($cuaca_tropodo);
echo '<h2>KEDUNGBANTENG</h2>
<div class="table-responsive">
<table class="table table-bordered">
<tr>';
foreach ($cuaca_tropodo as $cuaca) {
    if (strpos($cuaca->datetime, date("Y-m-d")) !== false) {
        // print_r($cuaca);
        echo '<td>
        Jam: ' . date("H:i", strtotime($cuaca->datetime)) . '<br>
        <img src="' . $cuaca->image . '" width="50px"/>
        ' . $cuaca->weather_desc . '<br>
        Suhu: ' . $cuaca->t . '°C<br>
        <img src="' . base_url("public/raindrop.png") . '" style="width:17px;"/>&nbsp;' . $cuaca->hu . '%
        </td>';
    }
}
echo '</tr></table></div>';
?>
<div id="datacam1" style="text-align:center;">
    <img id="cam1" style="max-width:600px;width:100%;" />
</div>
<br><br>
<?php
$bmkg_tropodo = file_get_contents("https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4=35.15.18.2005");
$area_tropodo = json_decode($bmkg_tropodo);
$cuaca_tropodo = $area_tropodo->data[0]->cuaca[0];
// print_r($cuaca_tropodo);
echo '<h2>TAMBAKSAWAH</h2>
<div class="table-responsive">
<table class="table table-bordered">
<tr>';
foreach ($cuaca_tropodo as $cuaca) {
    if (strpos($cuaca->datetime, date("Y-m-d")) !== false) {
        // print_r($cuaca);
        echo '<td>
        Jam: ' . date("H:i", strtotime($cuaca->datetime)) . '<br>
        <img src="' . $cuaca->image . '" width="50px"/>
        ' . $cuaca->weather_desc . '<br>
        Suhu: ' . $cuaca->t . '°C<br>
        <img src="' . base_url("public/raindrop.png") . '" style="width:17px;"/>&nbsp;' . $cuaca->hu . '%
        </td>';
    }
}
echo '</tr></table></div>';
?>

<div id="datacam2" style="text-align:center;">
    <img id="cam2" style="max-width:600px;width:100%;" />
</div>
<script>

    setInterval(() => {
        $("#cam1").attr('src', 'https://device.alfianrek.my.id/api/get/image/2ccf6729aa9e/');
        $("#cam2").attr('src', 'https://device.alfianrek.my.id/api/get/image/2ccf6729aa10/');
    }, 300);


</script>