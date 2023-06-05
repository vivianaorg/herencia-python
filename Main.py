from Persona import Persona
from Deportista import Deportista
from Futbolista import Futbolista
from Portero import Portero

print("\n****Inicia la creación de objetos con parametros****\n")
obj1 = Persona("Luis")
obj2 = Deportista("Pedro", 25)
obj3 = Futbolista("Miguel", 25, 12)
obj4 = Portero("Rene", 38, 1, 0)

print("\n****Inicia la creación de objetos default****\n")
obj5 = Persona()
obj6 = Deportista()
obj7 = Futbolista()
obj8 = Portero()