edad = int(input("Digita tu edad: "))
ingresos = int(input("¿Cuales sin tus ingresos mensuales? "))

def paga_inpuesto(e,i):
    if e >= 16 and i >= 1000:
        print("Usted debe tributar impuesto")
    elif e>=16 and i<1000:
        print("No tiene que tributar, no cuenta con suficientes ingresos")
    elif e<=16 and i>=1000:
        print("No debe tributar impuesto, es menor de edad")
    elif e<=16 and i<1000:
        print("No debe tributar, es menor de edad y no genera suficientes ingresos")

def run():
    paga_inpuesto(edad, ingresos)

if __name__ == '__main__':
    run()
