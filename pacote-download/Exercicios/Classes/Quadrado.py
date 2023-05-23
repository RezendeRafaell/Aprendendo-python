'''
Classe Quadrado: Crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''

class Quadrado:
    def __init__(self, lado):
        self._lado = lado
    
    def setLado(self, lado):
        self._lado = lado

    def getLado(self):
        return self._lado
    
    def calcularArea(self):
        return self._lado * self._lado

# Teste    
quadrado = Quadrado(3)

print (quadrado.getLado())
print(quadrado.calcularArea())
 
quadrado.setLado(12)
print (quadrado.getLado())
print (quadrado.calcularArea())
