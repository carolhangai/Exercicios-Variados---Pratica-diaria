#Faça uma lista de compras com While

print('Digite sua lista de compras.')
print('Para sair digite fim!')
compras = []
while True:   
     produto = input('Produto:')          
     if produto == "fim":
         break
     compras.append(produto)
for lista in compras:
     print(lista)
