# Strings

mi_string = "Hola mundo"
#print(dir(mi_string))

print(mi_string.upper())
print(mi_string.lower())
print(mi_string.capitalize())

print(mi_string.replace('Hola','bye').upper())
numero_de_l = mi_string.count('o')
print(numero_de_l)

if mi_string.startswith('Hola'):
    print("El texto empieza con Hola")
  

print(mi_string.split('o'))     # Divide el string
print(mi_string.find('o'))      # Encuentra la posición del caracter

print(len(mi_string))

print(mi_string[1])

print("Hola " + mi_string)
print(f"Hola {mi_string}")