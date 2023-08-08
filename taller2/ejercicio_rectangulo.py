class Rectangulo:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        #esquinas (x1,y1) y (x2, y2)
        self. x1: int = x1
        self. y1: int = y1
        self. x2: int = x2
        self. y2: int = y2
        self.dist_x: int = abs(self.x2 - self.x1)
        self.dist_y: int = abs(self.y2 - self.y1)

    def calcular_perimetro(self):
        #suma de los lados
        perimetro = 2*(self.dist_x+self.dist_y)
        return perimetro

    def calcular_area(self):
        #producto de base y altura
        area = self.dist_x*self.dist_y
        return area

    def es_cuadrado(self):
        if self.dist_x == self.dist_y:
            print("Es un cuadrado")
        else:
            print("No es un cuadrado")

if __name__=="__main__":
    #objetos de la clase Rectangulo
    puntos1: Rectangulo = Rectangulo(2,4,4,2)
    puntos1.es_cuadrado()

    puntos2: Rectangulo = Rectangulo(2,3,4,7)
    puntos2.es_cuadrado()
