'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome,peso e, peso e altura

Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

from pprint import pprint


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.005

        return self.idade

    def engordar(self, kg):
        self.peso += kg
        return self.peso
# Teste


joao = Pessoa('João', 10, 48, 1.50)
joao.envelhecer()
print(joao.__dict__)

joao.engordar(12)
print(joao.__dict__)
joao.envelhecer()
pprint(joao.__dict__)
print(joao.__dict__)
