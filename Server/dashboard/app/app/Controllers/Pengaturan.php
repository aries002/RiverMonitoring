<?php

namespace App\Controllers;

use App\Libraries\Template;
use App\Libraries\Atable;

class Pengaturan extends SecureController
{

    protected $template;
    protected $atable;
    public function __construct()
    {
        $this->template = new Template();
        $this->atable = new Atable();
    }
    public function index()
    {
        $info = "";
        if (isset($_POST["passnow"], $_POST["passnew1"], $_POST["passnew2"])) {
            // cek pegawai
            $cek = $this->db->query("SELECT * FROM pegawai WHERE id=? AND password=?", array($_SESSION["username"], $_POST['passnow']));
            if ($cek->getNumRows() == 1) {
                if ($_POST["passnew1"] != "" && $_POST["passnew2"] != "" && $_POST["passnew1"] == $_POST["passnew2"]) {
                    $qry = $this->db->query("UPDATE pegawai SET password='" . $_POST["passnew1"] . "' WHERE id='" . $_SESSION["username"] . "'");
                    if ($qry) {
                        $info = "Berhasil merubah password";
                    } else {
                        $info = "Gagal merubah password";
                    }
                }
            }
        }

        $data = [
            'title' => "Pengaturan",
            'db' => $this->db,
            'atable' => $this->atable,
            'info' => $info
        ];

        $this->template->display('pengaturan', $data);
    }
}
