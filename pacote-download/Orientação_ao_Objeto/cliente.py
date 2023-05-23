class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome.title()

    # Eu poderia ter criado um método aqui chamado nome_maiúsculo(), mas a questão é que quando
    # eu for chamar esse método, vai ser paia pq eu queria dar um jeito de chamar só cliente.nome
    # invés de clinte.nome_maiúsculo().
    #
    # Pensando nisso, o python tem esse @property que indica
    # que este método repesenta uma propriedade (seja lá o que propriedade for... kkk).

    # Para isso funcionar, o método tem que ter o mesmo nome da variável que vai no self e ela
    # deve estar empacotada (__)

    # Esse método é um getter, agora vamos fazer para um setter:

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
