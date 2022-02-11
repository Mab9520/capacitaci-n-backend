class Persona:
    pass
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año


    def descripcion(self):
        return ' {} tiene {} '.format(self.nombre, self.año)

    def comentario(self, frase):
        return ' {} dice: {}'.format(self.nombre, frase)

name = input("Digita tu nombre: ")
edad = input("Digita tu edad: ")
fr = input("Dime la frase: ")
doctor = Persona(name, edad)
print(doctor.descripcion())
print(doctor.comentario(fr))