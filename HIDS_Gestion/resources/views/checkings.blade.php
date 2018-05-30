@extends('layouts.app')

@section('content')
<div class="container">

    <h2 class="page-header">La liste des vérifications :</h2>

    <div class="row">
        @foreach($checkings as $checking)
            <div class="col-md-10 col-md-offset-1">
                <div class="panel panel-default">
                    <div class="panel-heading">{{ $checking->created_at }}</div>
                    <div class="panel-body">
                        <div class="row">
                            <div class="col-sm-10">
                                @if($checking->result)
                                    <p><span class="glyphicon glyphicon-ok-sign" aria-hidden="true"></span> La vérification n'a retournée aucune erreur.</p>
                                @else
                                    <p><span class="glyphicon glyphicon-remove-sign" aria-hidden="true"></span> La vérification a retournée une ou plusieurs erreurs.</p>
                                @endif
                            </div>
                            <div class="col-sm-2">
                                <form action="{{ url('/checking') }}" method="post">
                                    <input type="hidden" name="id" value="{{ $checking->id }}" />
                                    <input type="hidden" name="_token" value="{{ csrf_token() }}">
                                    <input type="submit" class="btn btn-primary btn-block" value="Détails"/>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        @endforeach
    </div>
</div>
@endsection
