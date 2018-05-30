<?php

namespace App\Http\Controllers;

use Faker\Provider\DateTime;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\DB;

class HomeController extends Controller
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


    public function addWebsite(Request $request)
    {
        // Insertion du site
        $id = DB::table('websites')->insertGetId(
            ['name' => $request->name,
                'url' => $request->url,
                'login_connection' =>$request->login,
                'password_connection' =>$request->password,
                'desc' => $request->desc,
                'configuration' =>  $request->conf_path,
                'folder_exception' => $request->conf_folders,
                'user_id' => Auth::id()]
        );


        /*// Ajout dela configuration
        $configuration = 'numSite|'.$id.'|pathToHash|'.$request->conf_path.'|pathSourceFile|'.$request->conf_outputPath.'|sourceFileName|'.'output.txt';

        //$request->folder_exception


        DB::table('websites')
            ->where('id', $id)
            ->update(
                ['configuration' => $configuration,
                    'folder_exception' => $request->conf_folders]
            );
*/

        return redirect('/');
    }

    public function removeWebsite(Request $request)
    {
        DB::table('websites')->where('id', '=', $request->id)->delete();
        return redirect('/');
    }


    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $websites = DB::table('websites')->get();
        return view('home', ['websites' => $websites]);
    }

    public function create_source(Request $request)
    {
        $id = DB::table('websites')->where('id', '=', $request->id);

        exec("sshpass -p 123456 ssh root@". $id." python /home/divinix/create_checksum_source.py");

        $websites = DB::table('websites')->get();
        return view('home', ['websites' => $websites]);
    }
}
