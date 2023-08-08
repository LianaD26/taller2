import math


class Punto:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def mostrar_punto(self):
        return (self.x, self.y)
class Circulo:
    def __init__(self, centro: Punto, radio: int):
        self.centro: Punto = Punto(2,5)
        self.radio: int = radio
    def area_circulo(self):
        area = math.pi*(self.radio)**2
        return area

    def perimetro_circulo(self):
        perimetro = 2*math.pi*self.radio
        return perimetro

    def punto_circulo(self, x2: int, y2:int):
        #x**2+y**2=r**2
        if x2**2 + y2**2 == self.radio**2:
            print(f"El punto ({x2,y2}) pertenece al círculo")
        else:
            print(f"El punto ({x2, y2}) NO pertenece al círculo")

if __name__ == "__main__":
    circulo1: Circulo= Circulo()