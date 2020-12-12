from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from veiculos.models import Veiculo
from veiculos.forms import FormularioVeiculo
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from sistema.utilitarios import AutenticacaoObrigatoria

def home(request):
    return render(request, 'veiculos/index.html')

@method_decorator(login_required, name='dispatch')
class VeiculosList(ListView):
    model = Veiculo
    context_object_name = 'lista_veiculos'
    template_name = 'veiculos/listar.html'

@method_decorator(login_required, name='dispatch')
#@login_required
class VeiculosNew(CreateView):

    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculos/novo.html'
    success_url = reverse_lazy('listar-veiculos')

@method_decorator(login_required, name='dispatch')
class VeiculosEdit(UpdateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculos/editar.html'
    success_url = reverse_lazy('listar-veiculos')

@method_decorator(login_required, name='dispatch')
class VeiculosDelete(DeleteView):
    """
    View para a exclusão de veiculos.
    """
    model = Veiculo
    template_name = 'veiculos/deletar.html'
    success_url = reverse_lazy('listar-veiculos')

from veiculos.serializers import SerializadorVeiculo
from rest_framework.generics import ListAPIView

class VeiculosListAPI(ListAPIView):
    serializer_class = SerializadorVeiculo

    def get_queryset(self):
        return Veiculo.objects.all()