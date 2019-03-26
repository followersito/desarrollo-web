colors = ['red', 'green', 'blue']

numbers_list = list((1, 2, 3, 4))
print(numbers_list)

range_list = list(range(1, 11))
print(range_list)
# print(dir(range_list))      # Con dir obtenemos los metodos del tipo de dato 
print(len(colors))
print(colors[1])
print('violet' in colors)
colors[1] = 'violet'

colors.append('yellow')

colors.extend(['black','white'])

colors.insert(4, 'orange')

colors.insert(len(colors),'pink')
print(colors)

#colors.pop()
#colors.remove('color_a_remover')

colors.sort()
print(colors)

colors.sort(reverse=True)
print(colors)

print(colors.count('red'))

