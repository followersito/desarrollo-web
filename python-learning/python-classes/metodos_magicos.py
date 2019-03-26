class Usuario:
    def __new__(cls):
        print("Este metodo es el primero en ejecutarse")
        return super().__new__(cls)

    def __init__(self):
        print("Este metodo es el segundo que se ejecuta")

    def mostrar_password(self):
        print(self.__password)

    def __str__(self):
        return "Esto se imprime cuando intento mostrar el objeto"    

    def __getattr__(self, nombre):
        print("No se encontró el atributo")        

usuario = Usuario()
print(usuario)
print(usuario.apellido)
# usuario.nombre = 'Ivan'
# usuario.__password = 'Este ya no es un secreto'
# print(usuario.nombre)

