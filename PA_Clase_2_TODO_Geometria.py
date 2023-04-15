

class cuadrado:
    def __init__(self, lado):
        self.lado = lado 

    def perimetro(self):
        return self.lado * 4

class rectangulo(cuadrado):
    def __init__(self,lado, lado2):
        self.lado = lado
        self.lado2 = lado2 

    def perimetro(self):
        return 2*self.lado + 2*self.lado2
    




# Pruebas
c1 = cuadrado(6)
c2 = cuadrado(4)
print(c1.perimetro())
print(c2.perimetro())

r1 = rectangulo(3,4)
r2 = rectangulo(4,10)
print(r1.perimetro())
print(r2.perimetro())