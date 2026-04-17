while True:
 
 usuario = input("Cual es tu nombre de usuario?")

 if usuario == "Ariel" or usuario == "ariel":
    print("Usuario Correcto\n")
    break
 else:
   
    print("\nNombre de usuario incorrecto, ingrese denuevo nombre de usuario\n")
   

intento = 5


while intento > 0:
    
    password = input("Ingrese su clave:\n")
    
    if password =="123XD":

        print ("Contraseña Correcta, Bienvenido Usuario Ariel")
        
        break
    else:
        
        intento = intento -1

        print (f"\nIntento Fallido, te quedan,  {intento} intentos\n")

        if intento == 0:
           
            print("Acceso Denegado. Por favor comuniquese con nuestro call center")
