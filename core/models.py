from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

# unidades
class Unidade(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    horario_abertura = models.TimeField()
    horario_fechamento = models.TimeField()

    def __str__(self):
        return self.nome

# servicos
class Servico(models.Model):

    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name="servicos")
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    duracao = models.DurationField()

    def __str__(self):
        return self.nome

# agendamento 
class Agendamento(models.Model):
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='agendamentos_cliente', limit_choices_to={'tipo': 'CLIENTE'})
    barbeiro = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='agendamentos_barbeiro', limit_choices_to={'tipo': 'BARBEIRO'})
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)

    data = models.DateField()
    horario = models.TimeField()

    criado_em = models.DateTimeField(auto_now_add=True)

    STATUS = [
        ('AGENDADO', 'Agendado'),
        ('CONCLUIDO', 'Concluído'),
        ('CANCELADO', 'Cancelado'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='AGENDADO'
    )

    def __str__(self):
        return f'{self.cliente.username} - {self.data}'

