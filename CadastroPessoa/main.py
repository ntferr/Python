from pessoa import Pessoa
from persistencia import Persistencia

pessoa = Pessoa()
pessoa.nome = input('Digite seu nome: ')
pessoa.idade = int(input('Digite sua idade: '))
pessoa.estado = input('Digite seu estado: ')

p = Persistencia()

p.cadastrar(pessoa)
print(p.listar())
