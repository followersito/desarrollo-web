usuarios = {
    "cmelchor":"root", 
    "user":"1234"
}

usuario = input("Ingrese su usuario:")
password = input("Ingrese su contraseña:")

if usuario in usuarios:
    if usuarios[usuario] == password:
        print("Acceso otorgado")
    else:
        print("Usuario o contraseña incorrectos")
else:
    print("Usuario o contraseña incorrectos")

