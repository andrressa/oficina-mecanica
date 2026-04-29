from django.test import TestCase
from .models import Cliente

class ClienteTest(TestCase):
    def test_criar_cliente(self):
        cliente = Cliente.objects.create(nome="Teste", telefone="0000")
        self.assertEqual(cliente.nome, "Teste")
