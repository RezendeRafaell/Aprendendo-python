# conta = Conta(123, "Nico", 55.5, 1000)
# conta2 = Conta(321, "Marco", 100.0, 1000)

# conta.transfere(10.0, conta, conta2)

# conta.extrato()
# conta2.extrato()

"""
    Self é a referência que sabe encontrar aquele objeto (que está sendo construido na memória)
    self.vai_pra_lá -> é como se o self soubesse o endereço e o vai_pra_lá manda o python pro objeto
    Os atributos são as características que especificam uma classe
    Init = função construtora
    Lembrar do princípio da responsabilidade única de cada classe
"""


class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        # o "__" faz com que você não possa alterar o método diretamente, sem alterar o código.
        # Isso se chama encapsulamento o acessoa ao atributo
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular}")

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou o limite')

    def transfere(self, valor, origem, destino):
        origem.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "0001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '0001', 'Caixa': '104', 'Bradesco': '237'}
