<?php
/**
 * Created by PhpStorm.
 * User: gauth
 * Date: 22/03/2017
 * Time: 10:26
 */

namespace App;


use Illuminate\Notifications\Notifiable;

class Website
{
    use Notifiable;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'name', 'url', 'user',
    ];

}