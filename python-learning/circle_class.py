class Circle:

    @staticmethod
    def pi():
        return 3.1416           # Variable de clase

    def __init__(self, radius):
        self.radius = radius  
    
    def area(self):
        return self.radius * self.radius * self.pi()


circle1 = Circle(4)         #Instancia del objeto Circle
circle2 = Circle(2)

print(Circle.pi())

# print(circle1.__dict__)           para ver el contenido del diccionario del objeto
print("El area del primer circulo es:",circle1.area())
print("El area del segundo circulo es:",circle2.area())