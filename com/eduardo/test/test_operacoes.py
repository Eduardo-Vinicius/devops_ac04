from unittest import TestCase
from com.eduardo.operacoes import Operacoes

class TestOperacoes(TestCase):

    def setUp(self):
        self.operacoes = Operacoes()
		
    def test_soma(self):
        self.assertEqual(self.operacoes.soma([1,5]), 6, "Should be 6")
    
    def test_multi(self):
        self.assertEqual(self.operacoes.multi([1,4]), 8, "Should be 8")
    
    def test_maior(self):
        self.assertEqual(self.operacoes.numeroMaior(4,6), 6, "Should be 6")