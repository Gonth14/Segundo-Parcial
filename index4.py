# Preguntar nombre
while True:
    
      usuario = input("Por favor ingrese su nombre: ")
      
      if usuario == "Ariel" or usuario == "ariel":
       
       print("\nBienvenido: Ariel")
       break
      else:
          print("\nIngrese un nombre valido")


monto = int(input("\nIngrese valor de la compra: "))

if monto <= 0:
    print("\nError! el monto no puede ser negativo")

else:
    if monto < 10000:
        descuento = 0
    
    elif monto <= 50000:
        descuento = 0.10
        
    else:
        descuento = 0.20

descuento_aplicado = monto * descuento
total = monto - descuento_aplicado

print("\nBoleta")
print("Nombre: ", usuario)
print("Monto: ", monto)
print("descuento aplicado: ", descuento)
print("Total:", total)
