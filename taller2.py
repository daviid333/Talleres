# n1 = int(input ("Ingrese numero 1: "))
# n2 = int(input ("Ingrese numero 2: "))

# if n1>n2:
#     print(n2, n1)
# else:
#     print(n1, n2)
# ////////////////////////////////////////////////////////////////////

# minuto = float (input("Cuantos minutos demoro su llamda ? "))
# if minuto <= 3:
#     print("Su llamada tiene un coste de 200$")
# elif minuto > 3:
#     print(200 + ((minuto -3)*100))

# ////////////////////////////////////////////////////////////////////

# c1 = int(input ("Cuantos conejos blancos tienes?"))
# c2 = int(input ("CUantos conejos negros tienes ?"))
# y1 = int(input ("Cuantos conejos blancos vendió?"))
# y2 = int(input ("CUantos conejos negros vendió?"))
# p1 = 10000
# p2 = 5000
# print("Vendiste un total de", y1+y2, "conejos")
# print("tuviste unas ganancias de " , (y1*p1)+ (y2*p2))
# if y1 > y2:
#     print("El color más vendido fue el blanco ")
# elif y1 == y2:
#     print("Ambos colores de conejos se vendieron igual")
# else:
#     print("EL color mas vendido fue el negro")

# ////////////////////////////////////////////////////////////////////

# nota1 = float(input ("Ingresela primera nota?"))
# nota2 = float(input ("Ingresela segunda nota?"))
# nota3 = float(input ("Ingresela tercera nota?"))
# notaprevios = ((nota1 + nota2 + nota3) /3) * 0.60
# print("Nota previos:" , notaprevios)

# notat1 = float(input ("Ingrese la nota del primer trabajo"))
# notat2 = float(input ("Ingrese la nota del segundo trabajo"))
# notatrabajos = ((notat1 + notat2)/2)*0.40
# print("Nota trabajos:", notatrabajos)

# notafinal = (notatrabajos + notaprevios)
# print("Nota final:", notafinal)

# ////////////////////////////////////////////////////////////////////

# nombreart = str(input ("Nombre del Articulo: "))
# clave = int(input ("Clave: "))
# precio = float(input ("Precio: "))
# cantidad = int(input ("Cantidad: "))

# if clave == 1:
#     preciocondescuento = (precio - (precio*0.10))
#     print("El precio con descuento es: ", preciocondescuento)
# elif clave == 2:
#     preciocondescuento =(precio -(precio*0.20))
#     print("El precio con descuento es:", preciocondescuento)

# ////////////////////////////////////////////////////////////////////

# presupuesto = float(input("Ingrese el presupuesto anual: "))
# ppsi = float(input("Cuanto porcentaje (%) Psiquiatría: "))
# pped = float(input("Cuanto porcentaje (%) Pediatría: "))
# ptra = float(input("Cuanto porcentaje (%) Traumatología: "))
# if pped + ppsi + ptra == 100:
#     p1 = ((presupuesto*ppsi) /100)
#     p2 = ((presupuesto*pped) /100)
#     p3 = ((presupuesto*ptra) /100)
#     print("Al área de Psiquiatría le corresponde:", p1 , "Pediatría:", p2 , "Traumatología:", p3)
#     print("Para un total de :", p1+p2+p3)
# else:
#     print("Error, LA SUMA DE LOS PORCENTAJES DA MÁS DEL 100%")

# ////////////////////////////////////////////////////////////////////

ida = float(input("Para que día del mes actual necesita el pasaje de ida:"))
vuelta = float(input("Para que día del mes actual necesita el pasaje de vuelta:"))
kms = float(input("Cuantos km tiene el vuelo como trayectoría ?"))

if vuelta - ida >= 7:
    if kms >800:
        nato = ((kms*2.5)*0.30)    
        print("Se le aplicó un descuento del 30 a tu ticket y ahora vale:", nato)
    else:
        print("El valor de tu ticket es de:", (kms*2.5))
else:
        print("El valor de tu ticket es de:", (kms*2.5))