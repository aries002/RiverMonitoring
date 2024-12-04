<?php
require("helper.php");

$page = (isset($_GET['page'])) ? $_GET['page'] : null;
$key = (isset($_GET['key'])) ? $_GET['key'] : null;
$dev_id = (isset($_GET['dev_id'])) ? $_GET['dev_id'] : null;

switch ($page) {
    case 'status':
        # Terima dan kirim status perangkat
        $pesan = (isset($_POST['pesan'])) ? $_POST['pesan'] : null;
        $response = proses_pesan($pesan);
        
        print('');
        break;
    case 'sensor_data':
        $sensor_data = (isset($_POST['sensor_data'])) ? $_POST['sensor_data'] : null;
        proses_sensor_data($sensor_data);
        break;
    default:
        http_response_code(404)
        break;
}


