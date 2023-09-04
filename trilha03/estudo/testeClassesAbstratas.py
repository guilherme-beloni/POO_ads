from Forma import Forma
from Retangulo import Retangulo
from triangulo import TrianguloEquilatero

objR = Retangulo(25, 8)
print('------Retangulo------')
print (objR)
print("Area: " + str(objR.calcularArea()))
print("Perimetro: " + str(objR.calcularPerimetro())+ '\n\n\n')



print('------Triangulo------')
objT = TrianguloEquilatero(10, 15)
print (objT)
print("Area: " + str(objT.calcularArea()))
print("Perimetro: " + str(objT.calcularPerimetro()))