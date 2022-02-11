#Definimos la lista
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def elimina_multiplos(lista):
    #definimos una lista vacía para agregar los elementos de la nueva lista
    abc = []
    #para cada elemento de la lista
    for i in range(0, len(lista)):
        #si el elemento en la posición es multiplo de 3
        if i % 3 == 0:
            print("se deben eliminar:", lista[i])
        #caso contrario agrega los elementos a la nueva lista
        else:
            abc.append(lista[i])
    print("La lista resultante es:", abc)

#Función principal
def run():
    elimina_multiplos(abecedario)

if __name__ == '__main__':
    run()




