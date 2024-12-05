<?php
require("config.php");

$databaseHost       = $CONFIG['mysql']['host'];
$databaseName       = $CONFIG['mysql']['database'];
$databaseUsername   = $CONFIG['mysql']['username'];
$databasePassword   = $CONFIG['mysql']['password'];
$koneksi = mysqli_connect($databaseHost, $databaseUsername, $databasePassword, $databaseName); 

// function check_token($dev_id = '', $key = '') : bool {
//     if($dev_id == '' || $key == ''){
//         return FALSE;
//     }else{
//         $result = 
//     }
// }

// function proses_sensor_data($sensor_data){
//     if($sensor_data == null){
//         return;
//     }
//     $data = json_decode($sensor_data)
//     $result = mysqli_query($koneksi, "INSERT INTO sensor (dev_id, ")
// }

// function proses_pesan($pesan){
//     if($pesan == null){
//         return '';
//     }
    
// }