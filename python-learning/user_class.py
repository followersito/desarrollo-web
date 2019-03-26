#Ejemplo numero 2 de clases en Python

class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.__generate_password(password)      # Con el "__" se asigna como atributo privado y no permite modificaciones
        self.email = email
    
    def __generate_password(self, password):
        return password.upper()

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = self.__generate_password(value)

ivan = Usuario('cmelchor', 'root_password', 'ivanmelchormejia@gmail.com')
print(ivan.username)
# print(ivan.__password)
print(ivan.email)
print(ivan.password)
ivan.password="New password"
print(ivan.password)