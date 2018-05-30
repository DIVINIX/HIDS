@extends('layouts.app')

@section('content')
<div class="container">

    <div class="row page-header">
        <div class="col-md-10"><h2>La liste des sites internet :</h2></div>
        <div class="col-md-2"><a class="btn btn-lg btn-success" href="{{ url('/addWebsite') }}">Ajouter un site</a></div>
    </div>


    <div class="row">
        @foreach($websites as $website)
        <div class="col-md-10 col-md-offset-1">
            <div class="panel panel-default">
                <div class="panel-heading"><b>{{ $website->name }}</b> <em>{{ $website->url }}</em></div>
                <div class="panel-body">
                    <div class="row">
                        <div class="col-sm-8">{{ $website->desc }}</div>
                        <div class="col-sm-4">
                            <div class="row">
                                <div class="col-sm-6">
                                    <form action="{{ url('/checkings') }}" method="post">
                                        <input type="hidden" name="id" value="{{ $website->id }}" />
                                        <input type="hidden" name="_token" value="{{ csrf_token() }}">
                                        <input type="submit" class="btn btn-primary btn-block" value="Détails"/>
                                    </form>
                                </div>
                                <div class="col-sm-6">
                                    <form action="{{ url('/remWebsite') }}" method="post">
                                        <input type="hidden" name="id" value="{{ $website->id }}" />
                                        <input type="hidden" name="_token" value="{{ csrf_token() }}">
                                        <input type="submit" class="btn btn-danger btn-block" value="Supprimer"/>
                                    </form>
                                </div>
                                <div class="col-sm-6">
                                    <form action="{{ url('/treatment') }}" method="POST">
                                        <input type="hidden" name="id" value="{{ $website->id }}" />
                                        <input type="hidden" name="_token" value="{{ csrf_token() }}">
                                        <input type="submit" class="btn btn-success btn-block" value="Faire un test"/>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        @endforeach
    </div>
</div>
@endsection
