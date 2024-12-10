<?php

namespace App\Controllers;
use App\Libraries\Atable;

class Home extends BaseController
{

    protected $atable;

    public function __construct()
    {
        $this->atable = new Atable();
    }
    public function index()
    {
        // return view('home');
        return redirect()->to("home/login");
    }
    public function login()
    {
        if (isset($_POST['username'], $_POST['password'])) {
            if (isset($_SESSION['tokens'], $_SESSION['tokenses'], $_COOKIE['PHPSESSID'])) {
                $fphpses = $_COOKIE['PHPSESSID'];
                if ($_SESSION['tokens'] == $_POST['lgnid'] && $fphpses === $_SESSION['tokenses']) {
                    $username = $_POST['username'];
                    $password = sha1(md5(sha1($_POST['password'])));
                    $cek = $this->db->query("SELECT * FROM account WHERE username=? AND password=?", array($username, $password));
                    if ($cek->getNumRows() == 1) {
                        $_SESSION['username'] = $username;
                        $_SESSION['level'] = 1;
                        return redirect()->to(base_url('dashboard'));
                    }
                }
            }
        }

        $tokenses = base64_encode(openssl_random_pseudo_bytes(32));
        setcookie('PHPSESSID', $tokenses); // 86400 = 1 day
        $_SESSION['tokenses'] = $tokenses;
        $_SESSION['tokens'] = base64_encode(openssl_random_pseudo_bytes(32));

        return view('login');
    }
    public function logout()
    {
        unset($_SESSION['username']);
        session_destroy();
        return redirect()->to(base_url());
    }
}
