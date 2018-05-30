<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', 'HomeController@index');


Auth::routes();

// Websites
Route::get('/addWebsite', function () {
    return view('addWebsite');
});
Route::post('/addWebsite', 'HomeController@addWebsite');
Route::post('/remWebsite', 'HomeController@removeWebsite');


// Checkings
Route::post('/checkings', 'CheckingController@indexAll');
Route::post('/checking', 'CheckingController@index');

// Create source
Route::post('/create_source', 'CreateSourceController@index');

// Treatment
Route::post('/treatment', 'TreatmentController@index');