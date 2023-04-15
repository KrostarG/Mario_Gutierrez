def area_rectangulo(lado, alto):
  return(lado*alto)

def perimetro_rectangulo(lado,alto):  
  return(2*lado+2*alto)


def area_cuadrado(lado):
 return lado*lado


def perimetro_cuadrado(lado):
  return 4*lado


def area_circulo(radio):
  return(3.1415926535*radio*radio)


def perimetro_circulo(radio):
  return(2*3.1415926535*radio)


print("el area del cuadrado es ", area_cuadrado(7))

print("el area del circulo es ", area_circulo(5))

print("el area del rectangulo es ", area_rectangulo(4,6))

print("el perimetro del cuadrado es ", perimetro_cuadrado(7))

print("el perimetro del circulo es ", perimetro_circulo(5))

print("el perimetro del rectangulo es ", perimetro_rectangulo(4,6))