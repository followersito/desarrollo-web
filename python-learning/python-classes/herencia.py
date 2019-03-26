class Animal: 
    @property
    def terrestre(self):
        return True


class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(self.nombre)


class Felino(Animal):   #Clase padre 
    @property
    def garras_retractiles(self):
        return True

    def cazar(self):
        print("El felino está cazando...")


class Gato(Felino, Mascota): 
    def __init__(self, nombre):
        Mascota.__init__(self, nombre)
        self.nombre_gato = nombre

    def gato_cazador(self):
        if self.garras_retractiles == True:
            self.cazar()
        else:
            print("El gato no puede cazar...")

    # Sobreescritura del método 'mostrar_nombre' de la clase Mascota
    def mostrar_nombre(self):      
        Mascota.mostrar_nombre(self)        # ¡self siempre se incluye!
        print("El nombre del gato es",self.nombre)


class Jaguar(Felino):
   pass


# Instancias de clases
# gato = Gato()
# jaguar = Jaguar()

# print(gato.garras_retractiles)
# gato.gato_cazador()
# print(gato.terrestre)

gato = Gato("Patricio")
gato.mostrar_nombre()