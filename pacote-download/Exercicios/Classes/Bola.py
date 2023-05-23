'''
Classe Bola: Crie uma classe que modele uma bola:
Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''


class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, cor):
        self.cor = cor

    def mostraCor(self):
        print(self.cor)

# Teste de Classe


bola = Bola('Amarela', 10, 'plástico')
bola.mostraCor()
bola.troca_cor('Azul')
bola.mostraCor()
