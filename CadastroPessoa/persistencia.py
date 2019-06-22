from pessoa import Pessoa

class Persistencia():

    def cadastrar (self, pessoa):
        self.objeto = pessoa
        with open('arquivo.txt', 'a') as arquivo:
            self.nome = self.objeto.nome
            self.idade = str(self.objeto.idade)
            self.estado = self.objeto.estado
            arquivo.write('Nome: {0}\n'.format(self.nome))
            arquivo.write('Idade: {0}\n'.format(self.idade))
            arquivo.write('Estado: {0}\n'.format(self.estado))
            arquivo.write('----------------------')

    def listar (self):
        with open('arquivo.txt', 'r') as arquivo:
            dados = arquivo.read()
            return dados
