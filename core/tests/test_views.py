from django.test import TestCase, Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):
	def setUp(self):
		self.dados = {
			'nome': 'Luan Fernandes',
			'email': 'souluan@live.com',
			'assunto': 'Teste',
			'mensagem': 'Testando o formulário de contato'
		}
		self.client = Client()

	def test_form_valid(self):
		request = self.client.post(reverse_lazy('index'), data=self.dados)
		self.assertEquals(request.status_code, 302)

	def test_form_invalid(self):
		dados = {
			'nome': 'Luan Fernandes',
			'assunto': 'Teste',
		}
		request = self.client.post(reverse_lazy('index'), data=dados)
		self.assertEquals(request.status_code, 200)
