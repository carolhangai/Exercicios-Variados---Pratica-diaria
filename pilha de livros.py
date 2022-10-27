class livros():
    def __init__(self):
        self.dados = []
 
    def empilha(self, elemento):
        self.dados.append(elemento)
        print('Empilhar',elemento)
 
    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)
 
    def vazia(self):
        return len(self.dados) == 0

p = livros()
p.empilha('livro A')
p.empilha('livro B')
p.empilha('livro C')
p.empilha('livro D')
p.empilha('livro E')
p.empilha('livro F')
print ('Desempilha',p.desempilha())
print ('Desempilha', p.desempilha())
print ('Desempilha',p.desempilha())
print ('Desempilha',p.desempilha())
print ('Desempilha',p.desempilha())
print ('Desempilha',p.desempilha())


