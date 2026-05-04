EJERCICIO 1:

Desarolle un programa en python que permita calcular el valor final del bicicleteo (estacionamiento, parking)
y del candado para el entro civico que ofrece descuento para el guardado de sus bicis segun los dias de uso

valor inicial: motocicleta 15.000 mensual
               candado: 9.000 mensual

(EDITAR LOS VALORES DE DIA DE USO. CUARTA LINEA)

Dias de uso                 Estudiantes                                descuento

cantidad de dias                si                                        25%
mayor o igual a 20


Cantidad de dias
mayor o igual a 20              no                                        15%


entre 10 y 20                   si                                        15%


mayor o igual a 20              no                                         8%


(CONDICIONES PARA EL CANDADO)
condicion 1:Ademas el candado tiene una regla adicional. Los estudiantes tienen un descuento del 12% adicional pagando con tarjeta de credito
condicion 2: Si ademas la cantidad de dias es menor a 15. Obtendra solo un 5%

aplicar: entrada operaciones salidas y condiciones

si la cantidad de dias en menor a 10. el descuento es de 0%



EJERCICIO 2:

Desarolle un programa en python que permita ingresar 2 numeros enteros que indique rango de numero. (solicitar al usuario numeros)

El primero debe ser menor al segundo
luego el programa debe generar un numero aleatorio (al azar) entre el rango de los numeros

para hacer esto sigue las siguientes instrucciones:

From random import randint

n = randint (n1, n2)

La linea 1 le permite cargar la funcion randint, luego la linea numero 2 usa una funcion randint que permite generar un numero aleatorio
a modo de ejemplo randint(1,10). genero un numero aleatorio entre el 1 y el 10.

Un generador de numero aleatorio debe ajustar el numero para que el valor final sea adivinado por el usuario luego de 3 intentos

(si genera un numero impar debe ajustarlo para que sea divisible por un numero par)

NOTA: si el numero ajustado llega a quedar fuera del rango entonces el numero final debe dividirse por el limite inferior


