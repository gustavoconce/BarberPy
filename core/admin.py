from django.contrib import admin
from .models import Unidade, Servico, Agendamento


@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "telefone",
        "horario_abertura",
        "horario_fechamento",
    )

    search_fields = ("nome", "telefone")

    ordering = ("nome",)


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "preco",
        "duracao",
    )

    search_fields = ("nome",)

    ordering = ("nome",)


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = (
        "cliente",
        "barbeiro",
        "servico",
        "status",
    )

    list_filter = (
        "status",
        "servico",
    )

    search_fields = (
        "cliente__username",
        "barbeiro__username",
    )

    ordering = ("-criado_em",)