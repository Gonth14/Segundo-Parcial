#try

try:
    num1 = float(input("Por favor ingrese un numero: "))
    num2 = float(input("\nPor favor ingrese un numero: "))
  
    if num2 == 0:
        raise ZeroDivisionError
    
    resultado = num1/ num2
    print (f"\nEl resultado de esta division es: {resultado}")
except ValueError:
    print("\nError, ingresa un nuevo numero")

except ZeroDivisionError:
    print ("\nerror No se puede dividir por cero")



finally:
    print("\nFin del programa")

