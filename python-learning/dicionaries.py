# Un diccionario es un tipo de dato que nos permite definir un registro
# a partir de claves y valores (Objetos de la vida real)

product = {
    "name": "book",
    "quantity": 3,
    "price": 4.99
}

person = {
    "first_name": "Ivan",
    "last_name": "Melchor"
}

print(type(product))

print(person.items())

# Se puede eliminar de la misma forma que se han eliminado los arreglos anteriores

person.clear()
print(person)

products = [
    {"name": 'book', "price":10.99},
    {"name": 'laptop',"price":15}
]
print(products)
