class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(
            f'A conta de número {self.__numero} tem o saldo de {self.__saldo}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        # Não precisa do parâmetro origem, pois ele já é o próprio self
        self.sacar(valor)
        destino.depositar(valor)
