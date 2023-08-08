class CuentaBancaria():
    def __init__(self, num_cuenta: int, propietario: str, balance: int):
        self. num_cuenta: int = num_cuenta
        self. propietario: str = propietario
        self. balance: int = balance

    def depositar(self, deposito: int):
        #depositar cierto valor en la cuenta bancaria
        self.balance += deposito
        return self.balance

    def retirar(self, cantidad: int):
        #retirar cierto valor en la cuenta bancaria
        self.balance -= cantidad
        return self.balance

    def aplicar_cuota_manejo(self):
        return self.balance*0.2

    def mostrar_detalles(self):
        print(f"La cuenta {self.num_cuenta} perteneciente a {self.propietario} cuenta con un balance de: {self.balance}")

if __name__=="__main__":
    persona1: CuentaBancaria = CuentaBancaria(123456, "Liana Diaz", 0)
    persona1.mostrar_detalles()
    persona1.depositar(23000)
    persona1.mostrar_detalles()
    persona1.retirar(12000)
    persona1.mostrar_detalles()