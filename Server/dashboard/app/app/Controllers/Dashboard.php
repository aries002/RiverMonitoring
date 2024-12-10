<?php

namespace App\Controllers;

use App\Libraries\Template;

class Dashboard extends SecureController
{

    protected $template;
    public function __construct()
    {
        $this->template = new Template();
    }
    public function index()
    {
        $qdev = $this->db->query("SELECT * FROM device");

        $data = [
            'title' => "Dashboard",
            'device' => $qdev->getResult()
        ];

        $this->template->display('dashboard', $data);
    }
    public function slip($user = "")
    {
        $bulan = date("m");
        $tahun = date("Y");
        if (isset($_POST["tgl"])) {
            $tgl = explode("-", $_POST["tgl"]);
            $bulan = $tgl[0];
            $tahun = $tgl[1];
        }
        $data = [
            'title' => "Slip Gaji",
            'db' => $this->db,
            'bulan' => $bulan,
            'tahun' => $tahun,
            'username' => $user == "" ? $_SESSION["username"] : $user
        ];

        $this->template->display('slipgaji', $data);
    }
}
