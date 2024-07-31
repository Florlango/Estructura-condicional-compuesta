#Introducir los lados de un triángulo y visualizar por pantalla si dicho
#triángulo es equilátero, isósceles o escaleno.
lado_1 = float(input("Ingrese el valor del lado 1: "))
lado_2 = float(input("Ingrese el valor del lado 2: "))
lado_3 = float(input("Ingrese el valor del lado 3: "))
if lado_1 == lado_2 == lado_3 :
    print ("El triángulo ingresado es equilátero.")
elif lado_1 != lado_2 != lado_3 :
    print ("El triángulo ingresado es escaleno.")
else:
    print ("El triángulo ingresado es isósceles.")
