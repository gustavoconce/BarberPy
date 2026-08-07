from django.urls import path

from . import views

urlpatterns = [

    path(
        "",
        views.lista_unidades,
        name="lista_unidades",
    ),

    path(
        "servicos/<int:unidade_id>/",
        views.lista_servicos,
        name="lista_servicos",
    ),

    path(
        "barbeiros/<int:servico_id>/",
        views.lista_barbeiros,
        name="lista_barbeiros",
    ),

    path(
        "horarios/<int:barbeiro_id>/<int:servico_id>/",
        views.lista_horarios,
        name="lista_horarios",
    ),

    path(
        "confirmar/",
        views.confirmar_agendamento,
        name="confirmar_agendamento",
    ),

    path(
        "meus/",
        views.meus_agendamentos,
        name="meus_agendamentos",
    ),
    
    path(
    "data/<int:barbeiro_id>/<int:servico_id>/",
    views.escolher_data,
    name="escolher_data",
),
]