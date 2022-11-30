print('Digite nome do livro.')
print('Para sair digite "fim"!')
pilha = []
while True:   
     livro = input("Nome do livro:")          
     if livro == "fim":
         break
     pilha.append(livro)
     print("Insere novo livro:",pilha)
     
while len(pilha)>0:
      pilha.pop()
      print("Remove livro da pilha: ", pilha)   

