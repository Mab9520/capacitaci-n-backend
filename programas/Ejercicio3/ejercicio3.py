#definimos la lista
precios = [50, 75, 46, 22, 80, 65, 8]

#Función para encontrar el número mayor
def numero_mayor(p):
    print("el número mayor es:", max(p))

#Función para encontrar el número menor
def numero_menor(q):
    #usamos el método min 
    print("El numero menor es:", min(q))


def run():
    numero_mayor(precios)
    numero_menor(precios)

if __name__ == '__main__':
    run()

