@extends('layouts.app')

@section('content')
<div class="container">

    <!-- Titre -->
    <h2 class="page-header">Ajouter un site :</h2>

    <!-- Contenu -->
    <br>
    <form action="{{ url('/addWebsite') }}" method="post" class="form-horizontal">
        <div class="form-group">
            <label for="name" class="col-sm-2 control-label">Nom :</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" id="name" name="name" required/>
            </div>
        </div>
        <div class="form-group">
            <label for="url" class="col-sm-2 control-label">URL ou IP du site :</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" id="url" name="url" required/>
            </div>
        </div>
        <div class="form-group">
            <label for="login" class="col-sm-2 control-label">Login :</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" id="login" name="login" required/>
            </div>
        </div>
        <div class="form-group">
            <label for="password" class="col-sm-2 control-label">Mot de passe :</label>
            <div class="col-sm-10">
                <input type="password" class="form-control" id="password" name="password" required/>
            </div>
        </div>
        <div class="form-group">
            <label for="desc" class="col-sm-2 control-label">Description :</label>
            <div class="col-sm-10">
                <textarea id="desc" name="desc" class="form-control"></textarea>
            </div>
        </div>

        <br>
        <h4>Configuration</h4>
        <br>

        <div class="form-group">
            <label for="conf_path" class="col-sm-2 control-label">Chemin du dossier à vérifier :</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" id="conf_path" name="conf_path" required/>
            </div>
        </div>
        <div class="form-group">
            <label for="conf_folders" class="col-sm-2 control-label">Dossier à exclure (séparer avec des '|') :</label>
            <div class="col-sm-10">
                <textarea id="conf_folders" name="conf_folders" class="form-control" placeholder="exemple : uploads|tmp|vendor"></textarea>
            </div>
        </div>

        <br>
        <input type="hidden" name="_token" value="{{ csrf_token() }}">
        <div class="form-group">
            <div class="col-sm-offset-2 col-sm-10">
                <button type="submit" class="btn btn-default">Valider</button>
            </div>
        </div>
    </form>


</div>
@endsection
