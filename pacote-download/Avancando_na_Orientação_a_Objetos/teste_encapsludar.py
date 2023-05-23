class Livro:
    def __init__(self, nome, ano, paginas):
        self.__nome = nome.title()
        self.ano = ano
        self.paginas = paginas
        self.__like = 0

    @property
    def like(self):
        return self.__like

    def adicionar_like(self):
        self.__like += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


o_nome_do_vento = Livro('o nome do vento', 2016, 625)
o_nome_do_vento.adicionar_like()
o_nome_do_vento.adicionar_like()
o_nome_do_vento.adicionar_like()

'''
    >>>> o_nome_do_vento.like = 0 (Se eu fizer isso o código quebra, por isso que a gente usa o __. Usando o __ aí surge mais uma questão, o uso do proprety pra "reconhecer sem o __ como ser tivesse, não sei explicar muito bem isso aí não")
'''

print(f'Nome: {o_nome_do_vento.nome} - Ano: {o_nome_do_vento.ano} - Páginas: {o_nome_do_vento.paginas} -  Likes {o_nome_do_vento.like}')
