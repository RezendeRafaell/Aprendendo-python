'''
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)

Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

Crie um programa que utilize esta classe. 

Ele deve pedir ao usuário que informe as medidades de um local. 

Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
'''

class Retangulo:
    def __init__(self, A, B):
        self.setLados(A, B)
    
    
    def setLados(self, A, B):
        self.ladoA = A
        self.ladoB = B
    
    def getLados(self):
        return (self.ladoA, self.ladoB)
  
    def area(self):
        return self.ladoA * self.ladoB
    
    def perimetro(self):
        return self.ladoA + self.ladoB
    
    def quantidadePisos(self):
        return (self.ladoA * self.ladoB) / 9.66 #m^2
    
    def quantidadeCorrimao(self):
        return  self.ladoA + self.ladoB / 12 #m
    
    

A = 10
B = 220

retangulo = Retangulo(A, B)

print(retangulo.area())
print(retangulo.quantidadePisos())
print(retangulo.quantidadeCorrimao())


