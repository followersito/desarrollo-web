x = (1, 2, 3)

#print(type(x))
#print(x)

y = tuple((1, 2, 3, 4))
#print(y[1])

locations = {
    (35.12312, 39.000):"Tokyo",
    (38.1515, 32.000):"Guatemala"
}
print(locations)

colors = {'red', 'blue', 'yellow'}
print(colors)
print(type(colors))
colors.add('violet')
print(colors)
colors.remove('red')        # Eliminar elementos del set
colors.clear()              # Eliminar valores del set completo
print(colors)
del colors                  # Elimina el set
