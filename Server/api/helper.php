<?php
require("config.php");

$databaseHost       = $CONFIG['mysql']['host'];
$databaseName       = $CONFIG['mysql']['database'];
$databaseUsername   = $CONFIG['mysql']['username'];
$databasePassword   = $CONFIG['mysql']['password'];
$koneksi = mysqli_connect($databaseHost, $databaseUsername, $databasePassword, $databaseName); 

function proses_sensor_data($sensor_data){
    if($sensor_data == null){
        return;
    }

}

function proses_pesan($pesan){
    if($pesan == null){
        return '';
    }
    
}