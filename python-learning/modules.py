# 3 tipos de modulos
# Propios (Own modules)
# Descargados de internet (third party)
# Modulos de python (Pre-construidos)

from datetime import timedelta, date
from fmath import sumar, restar

print(date.today())

print(timedelta(minutes=70))

# fmath.sumar(1, 2)
# fmath.restar(1, 2)

num1 = input("Ingrese el número 1:")
num2 = input("Ingrese el número 2:")

sumar(int(num1), int(num2))