<?php
namespace App\Libraries;

use CodeIgniter\Libraries;

class Mpdflib
{

  function load($param = [])
  {
    require_once APPPATH . 'ThirdParty/mpdf/autoload.php';
    return new \Mpdf\Mpdf($param);
  }

}