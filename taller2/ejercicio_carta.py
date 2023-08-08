class Carta:
    def __init__(self, valor: str, pinta: str):
        self.valor: str = valor
        self.pinta: str = pinta


corazones = "corazones"
picas = "picas"
rombos = "rombos"
treboles = "tréboles"

if __name__ == "__main__":
    carta1 : Carta = Carta("A", corazones)
    carta2 : Carta = Carta(2, treboles)
