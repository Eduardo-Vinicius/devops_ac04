class Operacoes():

    def soma(self, valores):
        val = 0
        for v in valores:
            val = val + v
            
        return val
        
    def numeroMaior(self, valor1, valor2):
        maior = 0
        if valor1 > valor2:
            maior = valor1
            return valor1
        else: 
            maior = valor2
            return valor2
            
        return maior
    
  
    def multi(self, valores):
        val = 2
        for v in valores:
            val = val * v
        return val