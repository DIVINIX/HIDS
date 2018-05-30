<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class CheckingController extends Controller
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

    /**
     * Show the all checkings for one website.
     *
     * @return \Illuminate\Http\Response
     */
    public function indexAll(Request $request)
    {
        $checkings = DB::table('checkings')->where('website_id', '=', $request->id)->orderBy('id', 'desc')->get();
        return view('checkings', ['checkings' => $checkings]);
    }

    /**
     * Show the checking for one website.
     *
     * @return \Illuminate\Http\Response
     */
    public function index(Request $request)
    {
        $checking = DB::table('checkings')->where('id', '=', $request->id)->first();
        $website = DB::table('websites')->where('id', '=', $checking->website_id)->first();
        return view('checking', ['checking' => $checking, 'website' => $website]);
    }
}
