from Forma import Forma

class TrianguloEquilatero(Forma):
    def calcularArea(self):
        return (super().getAltura() * super().getAltura()) / 2

    def calcularPerimetro(self):
        return  3 * super().getAltura()
    