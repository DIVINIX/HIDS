<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\DB;

class TreatmentController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('auth');
    }

    public function index(Request $request)
    {
        $website = DB::table('websites')->where('id', '=', $request->id)->first();

        $ip = $website->url;
        $login = $website->login_connection;
        $password = $website->password_connection;

        exec("sshpass -p " . $password . " ssh " . $login . "@" . $ip . " python /home/divinix/create_checksum_treatment.py");
        exec("python /home/divinix/workspace/Projet_HIDS/HIDS_Python/compare_checksum.py");

        $checkings = DB::table('checkings')->where('website_id', '=', $request->id)->orderBy('id', 'desc')->get();

        return view('checkings', ['checkings' => $checkings]);
    }
}
