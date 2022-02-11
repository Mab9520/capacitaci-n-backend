#clase superior
class Pokemon:
    pass
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def descripcion(self):
        return '{} es un pokemon tipo: {}'.format(self.nombre, self.tipo)

#clase hija
class Pikachu(Pokemon):
    def ataque(self, ataque):
        return '{} tipo de ataque: {}'.format(self.nombre, ataque)

class Charmander(Pokemon):
    def ataque(self, ataque):
        return '{} tipo de ataque: {}'.format(self.nombre, ataque)

pokemon1 = Pikachu('pichu', 'electrico')
print(pokemon1.descripcion())
