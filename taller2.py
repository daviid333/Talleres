# n1 = (input ("Ingrese numero 1: "))
# n2 = (input ("Ingrese numero 2: "))
# if n1.isalpha():
#     print("Sea serio y no coloque letras")
# elif n2.isalpha():
#     print("No me intente bugear hpta")
# else:
#     nuv1 = float(n1)
#     nuv2 = float(n2)   
#     if nuv1>nuv2:
#         print(nuv2, nuv1)
#     else:
#         print(nuv1, nuv2)


# ////////////////////////////////////////////////////////////////////

# minuto = (input("Cuantos minutos demoro su llamada ? "))
# if minuto.isalpha():
#     print("Lo que ingresaste no es un numero valido")
# else:
#     minuto = float(minuto)
#     if minuto <= 3:
#         print("Su llamada tiene un coste de 200$")
#     elif minuto > 3:
#         print(200 + ((minuto -3)*100))

# ////////////////////////////////////////////////////////////////////
# conejos = int(input ("Cuantos conejos tienes?"))
# c1 = int(input ("Cuantos conejos blancos tienes?"))
# c2 = int(input ("CUantos conejos negros tienes ?"))
# p1 = 1000
# p2 = 5000
# if c1+c2> conejos or c1+c2<conejos:
#     print("No concuerdan los datos")
# else:
#     y1 = int(input ("Cuantos conejos blancos vendió?"))
#     if y1>c1:
#         print("NO puedes vender más conejos de los que tienes")
#     else: 
#         y2 = int(input ("CUantos conejos negros vendió?"))
#         if y2>c2:
#             print("NO puedes vender más conejos de los que tienes")
#         else:
#             print("Vendiste un total de", y1+y2, "conejos")
#             print("tuviste unas ganancias de " , (y1*p1)+ (y2*p2))
#             if y1 > y2:
#                 print("El color más vendido fue el blanco ")
#             elif y1 == y2:
#                 print("Ambos colores de conejos se vendieron igual")
#             else:
#                 print("EL color mas vendido fue el negro")

# ////////////////////////////////////////////////////////////////////

# nota1 = float(input ("Ingresela primera nota?"))
# if nota1 > 5 or nota1 < 1:
#     print("Estas ingresando valores que no son validos, intenta nuevamente")
# else:
#     nota2 = float(input ("Ingresela segunda nota?"))
#     if nota2 > 5 or nota1 < 1:
#         print("Estas ingresando valores que no son validos, intenta nuevamente")
#     else:
#         nota3 = float(input ("Ingresela tercera nota?"))
#         if nota3 > 5 or nota1 < 1:
#             print("Estas ingresando valores que no son validos, intenta nuevamente")
#         else:
#             notaprevios = ((nota1 + nota2 + nota3) /3) * 0.60
#             print("Nota previos:" , notaprevios)

#             notat1 = float(input ("Ingrese la nota del primer trabajo"))
#             if notat1 > 5 or nota1 < 1:
#                 print("Estas ingresando valores que no son validos, intenta nuevamente")
#             else:
#                 notat2 = float(input ("Ingrese la nota del segundo trabajo"))
#                 if notat2 > 5 or nota1 < 1:
#                     print("Estas ingresando valores que no son validos, intenta nuevamente")
#                 else:
#                     notatrabajos = ((notat1 + notat2)/2)*0.40
#                     print("Nota trabajos:", notatrabajos)

#                     notafinal = (notatrabajos + notaprevios)
#                     print("Nota final:", notafinal)

# ////////////////////////////////////////////////////////////////////

# nombreart = str(input ("Nombre del Articulo: "))
# clave = int(input ("Clave: "))
# precio = float(input ("Precio: "))
# cantidad = int(input ("Cantidad: "))
# if clave >2 or clave<1:
#     print("Estas ingresando una clave no valida")
# else:
#     if clave == 1:
#         preciocondescuento = (precio - (precio*0.10))
#         print("El precio con descuento es: ", preciocondescuento)
#     elif clave == 2:
#         preciocondescuento =(precio -(precio*0.20))
#         print("El precio con descuento es:", preciocondescuento)

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

# ida = int(input("Para que día del mes actual necesita el pasaje de ida:"))
# vuelta = int(input("Para que día del mes actual necesita el pasaje de vuelta:"))
# kms = int(input("Cuantos km tiene el vuelo como trayectoría ?"))

# if vuelta - ida >= 7:
#     if kms >800:
#         nato = ((kms*2.5)*0.30)    
#         print("Se le aplicó un descuento del 30 a tu ticket y ahora vale:", nato)
#     else:
#         print("El valor de tu ticket es de:", (kms*2.5))
# else:
#         print("El valor de tu ticket es de:", (kms*2.5))

# ////////////////////////////////////////////////////////////////////
#PUNTO #2 PERO SIN MATCH, solo con if

# num = float(input("Introduzca un numero:" ))
# if num>=1 and num<=10:
#     if num %2 ==0:
#         print("El numero es par")
#     else:
#         print("El numero es impar")
# else:
#     print("El numero esta fuera de rango")

# # ////////////////////////////////////////////////////////////////////

# num = float(input("Introduzca un numero:" ))
# if num>=1 and num<=10:
# match

