<?php

namespace App\Controllers;

use App\Models\UserModel;

class Tes extends BaseController
{
    public function __construct()
    {
        // =============
    }

    public function index()
    {
        echo "Hello";
    }

    public function coba()
    {
        $user = new UserModel();
        $qry = $user->getWhere(["username" => "admin"])->getResultArray();
        print_r($qry);
    }

    public function kueri()
    {
        $qry = $this->db->query("SELECT * FROM account");
        print_r($qry->getResult());
    }
}
