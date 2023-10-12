class Persona:
    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = genero
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)


# Definir personas
abuelo = Persona("Daniel", "Masculino")
abuela = Persona("", "Femenino")

padre = Persona("Felix", "Masculino")
madre = Persona("Juliana", "Femenino")

tio = Persona("Roberto", "Masculino")
tia = Persona("Irma", "Femenino")

prima1 = Persona("Abigail", "Femenino")
prima2 = Persona("Lizbeth", "Femenino")

hijo = Persona("Jonathan", "Masculino")
hija = Persona("Nicole", "Femenino")

# Establecer relaciones
abuelo.agregar_hijo(padre)
abuelo.agregar_hijo(tio)
abuela.agregar_hijo(madre)
abuela.agregar_hijo(tia)

padre.agregar_hijo(hijo)
madre.agregar_hijo(hija)

tio.agregar_hijo(prima1)
tia.agregar_hijo(prima2)

# Mostrar relaciones
print(f"Abuelo tiene {len(abuelo.hijos)} hijos: {', '.join([hijo.nombre for hijo in abuelo.hijos])}")
print(f"Padre tiene {len(padre.hijos)} hijo: {padre.hijos[0].nombre}")
print(f"Tío tiene {len(tio.hijos)} hijo: {tio.hijos[0].nombre}")