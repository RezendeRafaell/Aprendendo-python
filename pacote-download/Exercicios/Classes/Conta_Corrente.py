'''
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 

A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 

Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero (Como?) e os demais atributos são obrigatórios.

'''


class Conta:
    def __init__(self, conta, nome, saldo=0):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, nome):
        self.nome = nome

    def deposito(self, deposito):
        self.saldo += deposito

    def saque(self, saque):
        self.saldo -= saque

    def getConta(self):
        return [self.nome, self.conta]

    def getSaldo(self):
        return (self.saldo)


rafael = Conta(2, 'Rafael')
print(rafael.getConta())

rafael.deposito(1000)
print(rafael.getSaldo())

rafael.saque(1)
print(rafael.getSaldo())

rafael.alterarNome('João')
print(rafael.getConta())
