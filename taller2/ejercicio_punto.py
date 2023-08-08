import math


class Punto:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
    def mostrar_punto(self):
        print("Coordenadas: ",(self.x, self.y))

    def mover_punto(self, nuevo_x: int, nuevo_y: int):
        self.x: int = nuevo_x
        self.y: int = nuevo_y
        print("Nuevas coordenadas: ", (self.x, self.y))

    def calcular_distancia(self, x2: int, y2: int):
        #distancia del punto 1 a un nuevo punto
        d=math.sqrt((x2-self.x)**2 - (y2-self.y)**2)
        return d


if __name__=="__main__":
    #objetos de la clase Punto
    punto1: Punto = Punto(3,4)
    punto1.mostrar_punto()
    punto1.mover_punto(4,7)

    punto1.calcular_distancia(8,9)