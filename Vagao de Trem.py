"""Atividade professor Leandro"""

class vagao:
    def __init__(self,mercadoria):
        self.conteiner = mercadoria
        self.dianteiro = None
        self.trazeiro  = None

primeiro = vagao("Etanol")
i = 0
dianteiro = primeiro
while i <= 10:
    v = vagao("Gasolina "+str(i))    
    v.dianteiro = dianteiro
    dianteiro.trazeiro = v
    dianteiro = v
    i = i + 1
ultimo = v
    
 
ca = ultimo
while ca != None:    
    print(ca.conteiner)
    ca = ca.dianteiro    

