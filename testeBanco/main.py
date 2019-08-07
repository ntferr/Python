#!/usr/bin/python
from pessoa import Pessoa
from bd.connection import Connection

print('Digite seu nome: ')
nome = input()
print('Digite sua idade: ')
idade = int(input())

pessoa = Pessoa(nome, idade)

con = Connection()

#con.inserir(pessoa)
#print(con.consultar())
obj = con.consultar()
for i in obj:
    print(i)
