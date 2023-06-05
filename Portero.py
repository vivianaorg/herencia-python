from Futbolista import Futbolista

class Portero(Futbolista):
    def __init__(self, nombre='', edad=0, numero=1, goles=0):
        super().__init__(nombre, edad, numero)
        self.goles = goles
        print("Construyendo objeto Portero - " + str(id(self)))  # Esto es solo para hacer pruebas

    def getGoles(self):
        return self.goles

    def setGoles(self, goles):
        self.goles = goles