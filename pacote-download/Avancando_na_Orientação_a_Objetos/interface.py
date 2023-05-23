'''
A interface consiste em uma estrutura da linguagem que garante que todos que a implementarem terão a obrigação de implementar todos os métodos abstratos nela.


'''


# from abc import ABC  # abstract base classes

# from collections.abc import MutableSequence
# from numbers import Complex
# class Numero(Complex):
#     def __getitem__ (self, item):
#         super().__getitem__()


# filmes = Numero()

from collections.abc import Sized


class MinhaListagem(Sized):
    def __init__(self, descricao):
        self.descricao = descricao

    def __str__(self):
        return self.descricao


lista = MinhaListagem('Nova_lista')
print(lista)
