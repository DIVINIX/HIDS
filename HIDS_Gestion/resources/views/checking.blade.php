@extends('layouts.app')

@section('content')
<div class="container">

    <!-- Titre -->
    <h2 class="page-header"> {{ $website->name }} : {{ $checking->created_at }} </h2>

    <!-- Contenu -->
    @if($checking->result)
        <div class="alert alert-success" role="alert"><h3 class="text-center">{{ $checking->description }}</h3></div>
    @else
        <div class="alert alert-danger" role="alert"><h3 class="text-center">{{ $checking->description }}</h3></div>
    @endif

    <!-- Retour -->
    <div class="center-block text-center">
        <form action="{{ url('/checkings') }}" method="post">
            <input type="hidden" name="id" value="{{ $website->id }}" />
            <input type="hidden" name="_token" value="{{ csrf_token() }}">
            <input type="submit" class="btn btn-info btn-lg" value="Retour à la liste"/>
        </form>
    </div>


</div>
@endsection
