<?php
require("helper.php");

$page = (isset($_GET['page'])) ? $_GET['page'] : null;

switch ($page) {
    case 'status':
        # Terima dan kirim status perangkat
        $pesan = (isset($_POST['pesan'])) ? $_POST['pesan'] : null;
        $sensor_data = (isset($_POST['sensor_data'])) ? $_POST['sensor_data'] : null;
        proses_sensor_data($sensor_data);
        $response = proses_pesan($pesan);
        $ret -> status = 200;
        $response = json_encode($ret)
        break;
    
    default:
        http_response_code(404)
        break;
}


