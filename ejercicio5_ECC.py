#Realice un programa que pida un número del 1 al 12 y diga el nombre
#del mes correspondiente.

meses = {1:"Enero",
         2:"Febrero",
         3:"Marzo",
         4:"Abril",
         5:"Mayo",
         6:"Junio",
         7:"Julio",
         8:"Agosto",
         9:"Septiembre",
         10:"Octubre",
         11:"Noviembre",
         12:"Diciembre"}

numero = int(input("Ingrese un número del 1 al 12: "))

if 1<= numero <= 12:
    print (f"El mes ingresado es {meses[numero]}")

else: print ("El número ingresado no es válido.")


