#Pedimos el número al usuario, lo convertimos a número entero
numero = int(input("Digíte un numero: "))

#Función para verificar si el número es primo
def es_primo(num):
    #Variable que no servirá para contar por cuantos numeros es divisible
    n = 0
    #Ciclo para definir si el modulo es 0 suma uno al contador
    for i in range (1, num):
        if num % i == 0:
            n += 1
    #Si el contador es mayor o igual a dos el número es divisible en más numeros entonces no es primo
    if n >= 2:
        print("El número: ", num, " no es un número primo")
    else:
        print("El número: ", num, " es un número primo")
        
#Función principal
def run():
    es_primo(numero)

#entrypoint
if __name__ == '__main__':
        run()