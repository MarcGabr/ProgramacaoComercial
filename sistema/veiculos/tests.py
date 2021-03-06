from django.test import TestCase 
from django.urls import reverse 
from veiculos.models import * 
from veiculos.forms import *
from datetime import datetime

class TestViewVeiculosList(TestCase): 
    ''' 
    Classe de testes para a view VeiculosList 
    ''' 

    def setUp(self): 
        self.url = reverse('listar-veiculos') 
        Veiculo(marca='aaa', modelo='aaa', ano_fabricacao=1, modelo_fabricacao=2, combustivel=3, valor=4).save() 
        Veiculo(marca='fff', modelo='fff', ano_fabricacao=5, modelo_fabricacao=6, combustivel=7, valor=8).save() 

def test_get(self): 
        '''
        Testa o método GET da URL de listagem de veículos
        '''
        response = self.client.get(self.url) 
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(len(response.context.get('lista_veiculos')), 2)

class TestViewVeiculosNew(TestCase): 
    
    def setUp(self): 
        self.url = reverse('novo-veiculo') 

    def test_get(self): 
        response = self.client.get(self.url) 
        self.assertEqual(response.status_code, 302) 
        self.assertIsInstance(response.context.get('form'), FormularioVeiculo)

    def test_post(self):
        data = {
        'marca':'aaa', 'modelo':'aaa', 'ano_fabricacao':1, 'modelo_fabricacao':2, 'combustivel':3, 'valor':4
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 200)
        #self.assertRedirects(response, reverse('listar-veiculos'))
        
        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().marca, 'aaa')

class TestViewVeiculosEdit(TestCase):
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Veiculo)
        self.assertIsInstance(response.context.get('form'), FormularioVeiculo)
        self.assertEqual(response.context.get('object').pk, self.instance.pk)
        self.assertEqual(response.context.get('object').valor, 15000)

def test_post(self):
        data = {
            'marca': 'zzz', 
            'modelo': 'zzz', 
            'ano_fabricacao': 4, 
            'modelo_fabricacao': 3, 
            'combustivel': 2,
            'valor': 1
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))
        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().marca, 'zzz')
        self.assertEqual(Veiculo.objects.first().pk, self.instance.pk)

class TestViewVeiculosDelete(TestCase):
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Veiculo)
        self.assertEqual(response.context.get('object').pk, self.instance.pk)
    def test_post(self):
        response = self.client.post(self.url)

        # Verifica se apos a exclusao houve um redirecionamento para a view VeiculosList
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))
        self.assertEqual(Veiculo.objects.count(), 0)

class TestModelVeiculo(TestCase):
    def setUp(self):
        self.instance = Veiculo(marca='fff', modelo='fff', ano_fabricacao= datetime.now().year, modelo_fabricacao=6, combustivel=7, valor=8).save() 
    def test_is_new(self):
        self.assertTrue(self.instance.veiculo_novo)
        self.instance.ano_fabricacao = datetime.now().year - 5
        self.assertFalse(self.instance.veiculo_novo)
    def test_years_use(self):
        self.assertEqual(self.instance.anos_de_uso, 0)
        self.instance.ano_fabricacao = datetime.now().year - 5
        self.assertEqual(self.instance.anos_de_uso, 5)