def validar_nombre():
    nombre = input("Ingrese su nombre")

    while len (nombre) < 3:
        print("error el nombre debe tener al menos 3 caracteres")
        nombre = input("ingrese su nombre")

        return nombre
    
    nombre = validar_nombre