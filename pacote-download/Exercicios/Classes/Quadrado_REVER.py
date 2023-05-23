'''
Classe Quadrado: Crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''
class Quadrado:
    def __init__(self, lado):
        self._lado = lado
    
    @property
    def lado(self):
        return self._lado

    @lado.setter
    def lado(self, novo_lado):
        self._lado = novo_lado
        
    
    def area(self):
        return print(f'O valor do lado é {self.lado} e a área é {self.lado ** 2}')

    
#Teste
quadrado = Quadrado(3)
quadrado.area()
quadrado.lado(2)

# print(quadrado.lado)
