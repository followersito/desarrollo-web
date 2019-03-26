class Animal: 
    @property
    def terrestre(self):
        return True

class Felino(Animal):   #Clase padre 
    @property
    def garras_retractiles(self):
        return True

    def cazar(self):
        print("El felino está cazando...")

class Gato(Felino): 
    def gato_cazador(self):
        if self.garras_retractiles == True:
            self.cazar()
        else:
            print("El gato no puede cazar...")

class Jaguar(Felino):
   pass

# Instancias de clases
gato = Gato()
jaguar = Jaguar()

print(gato.garras_retractiles)
gato.gato_cazador()
print(gato.terrestre)