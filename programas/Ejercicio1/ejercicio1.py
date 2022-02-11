#Definimos la lista
asignaturas = ["Español", "Matemáticas", "Física", "Quimica", "Inglés", "Historia"]

#Función para imprimir el mensaje
def imprime_asignatura(a):
    for i in range(0,len(a)):
        print("Yo estudio", a[i])

#Función principal
def run():
    imprime_asignatura(asignaturas)

if __name__ == '__main__':
    run()
