@extends('layouts.app')

@section('content')
    <div class="container">

        <!-- Titre -->
        <h2 class="page-header"> Site : {{ $website->name }} </h2>

        <!-- Contenu -->
        <p> Création des checksums source réussi.</p>

    </div>
@endsection
