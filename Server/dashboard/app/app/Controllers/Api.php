<?php

namespace App\Controllers;

use CodeIgniter\RESTful\ResourceController;
use CodeIgniter\API\ResponseTrait;

class Api extends ResourceController
{
    use ResponseTrait;
    public function index()
    {
        $data = [
            "status_code" => 200,
            "message" => "Hello"
        ];
        return $this->respond($data);
    }
}
