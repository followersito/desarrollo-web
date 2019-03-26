class Persona:
    def __init__ (self, dpi, nombre, apellido, tiene_voz):
        self.dpi = dpi
        self.nombre = nombre
        self.apellido = apellido
        self.tiene_voz = tiene_voz

    def hablar(self):
        if self.puede_hablar() == True:
            print("La persona está hablando...")
        else:
            print("La persona no puede hablar")

    def caminar(self):
        print("La persona está caminando...")

    def puede_hablar(self):
        print(self.tiene_voz)
        return self.tiene_voz


# Se crea la instancia de la clase (Objeto)
persona = Persona("3003-41644-0101", "Ivan", "Melchor", False)
print(persona.dpi)
persona.hablar()
persona.caminar()
