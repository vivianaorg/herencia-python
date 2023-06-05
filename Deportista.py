from Persona import Persona

class Deportista(Persona):
    
    def __init__(self, nombre='', edad=0):
        super().__init__(nombre)
        self.edad = edad
        print("Construyendo objeto Deportista - " + str(id(self)))  # Esto es solo para hacer pruebas

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad
        
    