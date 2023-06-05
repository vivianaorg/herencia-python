class Persona:
    def __init__(self, nombre=""):
        self.nombre = nombre
        print("Construyendo objeto Persona - " + str(id(self)))  # Esto es solo para hacer pruebas

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre