import re 
for n in range(0,3): 
  n = str(input("Digite seu nome e sobrenome:")).strip()
  print("Olá, meu nome é", n)
  print("Com expressão regular")  
  nome = n.split()
  print(nome)
  print("Sem expressão regular")
  print(nome[0])

 