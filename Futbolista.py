from Deportista import Deportista

class Futbolista(Deportista): 
    
    def __init__(self, nombre='', edad=0, numero=1):
        super().__init__(nombre, edad)
        self.numero = numero
        self.Deportista = []

    def getNumero(self):
        return self.numero

    def setNumero(self, numero):
        self.numero = numero
        
    def agregarDeportista(self, nombre, edad):
        for Deportista in self.Deportista:
            if Deportista.getNombre() == nombre or Deportista.getEdad() == edad:
                return False
        
        nuevoDeportista = Deportista(nombre, edad)
        self.estudiantes.append(nuevoDeportista)
        return True
    
    def eliminarDeportista(self, Deportista):
        if Deportista in self.Deportista:
            self.Deportista.remove(Deportista)
        