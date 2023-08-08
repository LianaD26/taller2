class Vehiculo:
    def __init__(self, vel_max: float, km: int):
        self.vel_max: float = vel_max
        self.km: int = km

    def Mostrar_vehiculo(self):
        print("kilometros: ", self.km)
        print("velocidad máxima: ", self.vel_max)


if __name__=="__main__":
    #objetos de la clase vehículo
    toyota: Vehiculo = Vehiculo(34.5, 45)
    toyota.Mostrar_vehiculo()