class Figura:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def datos_figura(self):
        return 'La figura tiene una base de: {} y una altura de: {}'.format(self.base, self.altura)

class Cuadrado(Figura):  
    def perimetro_cuadrado(self):
        perimetro = 0
        perimetro = self.base + self.altura + self.base + self.altura
        return 'El perímetro del cuadrado es: {}'.format(perimetro)
    
    def area_cuadrado(self):
        area = 0
        area = self.base * self.altura
        return 'El área del cuadrado es: {}'.format(area)

class Rectangulo(Figura):
    def perimetro_rectangulo(self):
        perimetro = 0
        perimetro = self.base + self.altura + self.base + self.altura
        return 'El perímetro del rectángulo es: {}'.format(perimetro)
    
    def area_rectangulo(self):
        area = 0
        area = self.base * self.altura
        return 'El área del rectángulo es: {}'.format(area)

class Triangulo(Figura):
    def perimetro_triangulo(self):
        perimetro = 0
        perimetro = self.base + self.altura + self.base 
        return 'El perímetro del triangulo es: {}'.format(perimetro)
    
    def area_triangulo(self):
        area = 0
        area = (self.base * self.altura)/2
        return 'El área del triángulo es: {}'.format(area)

cuadrado = Cuadrado(2,2)
print(cuadrado.datos_figura())
print(cuadrado.perimetro_cuadrado())
print(cuadrado.area_cuadrado())

rectangulo = Rectangulo(3, 2)
print(rectangulo.datos_figura())
print(rectangulo.perimetro_rectangulo())
print(rectangulo.area_rectangulo())

triangulo = Triangulo(3, 4)
print(triangulo.datos_figura())
print(triangulo.perimetro_triangulo())
print(triangulo.area_triangulo())




    


