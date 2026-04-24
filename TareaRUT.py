def calcular_dv(rut_num):
    suma = 0
    multiplicador = 2

    for digito in reversed(str(rut_num)):
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    resto = 11 - (suma % 11)

    if resto == 11:
        return '0'
    elif resto == 10:
        return 'K'
    else:
        return str(resto)



intentos_rut = 5
rut_valido = False

while intentos_rut > 0 and not rut_valido:
    try:
        rut_input = input("Ingrese su RUT (ej: 12345678-5): ")

        if "-" not in rut_input:
            raise ValueError("Formato incorrecto")

        rut_num, dv_ingresado = rut_input.split("-")
        dv_ingresado = dv_ingresado.upper()

        if not rut_num.isdigit():
            raise ValueError("El RUT debe ser numérico")

        dv_real = calcular_dv(rut_num)

        if dv_real == dv_ingresado:
            print("RUT válido")
            rut_valido = True
        else:
            intentos_rut -= 1
            print("RUT inválido")
            print("Intentos restantes RUT:", intentos_rut)

    except Exception as e:
        intentos_rut -= 1
        print("Error:", e)
        print("Intentos restantes RUT:", intentos_rut)



if not rut_valido:
    print("Acceso bloqueado por demasiados intentos fallidos de RUT")

else:
    
    intentos_clave = 5
    acceso = False

    while intentos_clave > 0 and not acceso:
        try:
            clave = input("Ingrese su clave (10 dígitos): ")

            if len(clave) == 10 and clave.isdigit():
                print("Acceso permitido")
                acceso = True
            else:
                intentos_clave -= 1
                print("Clave inválida")
                print("Intentos restantes clave:", intentos_clave)

        except Exception as e:
            intentos_clave -= 1
            print("Error:", e)
            print("Intentos restantes clave:", intentos_clave)

    if not acceso:
        print("Acceso bloqueado por demasiados intentos fallidos")