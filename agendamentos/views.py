from django.shortcuts import render
from core.models import Unidade, Servico, Agendamento
from usuarios.models import Usuario
from datetime import datetime, timedelta
from django.utils import timezone
from datetime import datetime


def lista_unidades(request):

    unidades = Unidade.objects.all()

    return render(
        request,
        "agendamentos/lista_unidades.html",
        {
            "unidades": unidades
        }
    )


def lista_servicos(request, unidade_id):

    unidade = Unidade.objects.get(id=unidade_id)

    servicos = Servico.objects.filter(
        unidade=unidade
    )

    return render(
        request,
        "agendamentos/lista_servicos.html",
        {
            "unidade": unidade,
            "servicos": servicos,
        }
    )


def lista_barbeiros(request, servico_id):

    servico = Servico.objects.get(id=servico_id)

    barbeiros = Usuario.objects.filter(
        tipo="BARBEIRO"
    )

    return render(
        request,
        "agendamentos/lista_barbeiros.html",
        {
            "servico": servico,
            "barbeiros": barbeiros,
        },
    )


from datetime import time


def lista_horarios(request, barbeiro_id, servico_id):

    barbeiro = Usuario.objects.get(id=barbeiro_id)
    servico = Servico.objects.get(id=servico_id)

    data_str = request.GET.get("data")

    if not data_str:
        return redirect(
            "escolher_data",
            barbeiro_id=barbeiro.id,
            servico_id=servico.id,
        )

    data = datetime.strptime(
        data_str,
        "%Y-%m-%d"
    ).date()

    agendamentos = Agendamento.objects.filter(
        barbeiro=barbeiro,
        data=data,
        status="AGENDADO"
    )

    horarios_ocupados = [
        agendamento.horario
        for agendamento in agendamentos
    ]

    horarios = [
        time(8, 0),
        time(8, 30),
        time(9, 0),
        time(9, 30),
        time(10, 0),
        time(10, 30),
        time(11, 0),
        time(11, 30),
        time(12, 0),
        time(12, 30),
        time(13, 0),
        time(13, 30),
        time(14, 0),
        time(14, 30),
        time(15, 0),
        time(15, 30),
        time(16, 0),
        time(16, 30),
        time(17, 0),
        time(17, 30),
        time(18, 0),
        time(18, 30),
        time(19, 0),
    ]

    horarios_disponiveis = [
        horario
        for horario in horarios
        if horario not in horarios_ocupados
    ]

    return render(
        request,
        "agendamentos/lista_horarios.html",
        {
            "barbeiro": barbeiro,
            "servico": servico,
            "horarios": horarios_disponiveis,
            "data": data,
        },
    )
def confirmar_agendamento(request):

    return render(
        request,
        "agendamentos/confirmar_agendamento.html"
    )


def meus_agendamentos(request):

    return render(
        request,
        "agendamentos/meus_agendamentos.html"
    )



def escolher_data(request, barbeiro_id, servico_id):

    barbeiro = Usuario.objects.get(id=barbeiro_id)
    servico = Servico.objects.get(id=servico_id)

    return render(
        request,
        "agendamentos/escolher_data.html",
        {
            "barbeiro": barbeiro,
            "servico": servico,
        },
    )