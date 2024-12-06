<?php
namespace App\Libraries;

use CodeIgniter\Libraries;

class Template
{
	function __construct()
	{

	}

	function display($content = "", $data = [])
	{
		$template['_header'] = view('template/header', $data);
		$template['_sidebar_menu'] = view('template/sidebar_menu', $data);
		$template['_content'] = view($content, $data);
		$template['_footer'] = view('template/footer', $data);
		echo view('template/index', $template);
	}
}
/* End of file template.php */
/* Location: ./application/libraries/template.php */