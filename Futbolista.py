from Deportista import Deportista

class Futbolista(Deportista):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.numero = None

    def getNumero(self):
        return self.numero

    def setNumero(self, numero):
        self.numero = numero

    def agregarDeportista(self, nombre, edad):
        for deportista in self.deportistas:
            if deportista.getNombre() == nombre or deportista.getEdad() == edad:
                return False

        nuevoDeportista = Deportista(nombre, edad)
        self.deportistas.append(nuevoDeportista)
        return True

    def eliminarDeportista(self, deportista):
        if deportista in self.deportistas:
            self.deportistas.remove(deportista)




        