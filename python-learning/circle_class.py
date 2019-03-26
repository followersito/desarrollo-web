class Circle:

    _PI = 3.1416           # Variable de clase

    def __init__(self, radius):
        self.radius = radius  
    
    def area(self):
        return self.radius * self.radius * self._PI


circle1 = Circle(4)
circle2 = Circle(2)

# print(circle1.radius)
# print(circle2.radius)
# print(Circle.PI)        # No es necesario crear un objeto para usar y acceder a PI

print(circle1.__dict__)
print("El area del circulo es:",circle1.area())

print(circle2.__dict__)
print("El area del segundo circulo es:",circle2.area())