"""Atividade IFPR"""
pilha_livro = []


pilha_livro.append('Livro 1')
pilha_livro.append('Livro 2')
pilha_livro.append('Livro 3')  
print('Empilhar',pilha_livro)


while pilha_livro:
    livro = pilha_livro.pop()
    print('Desempilha',livro)
