#Realice un programa que lea tres números, muestre cuál es el mayor y
#determine si es par o impar.
numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))
numero_3 = int(input("Ingrese el tercer número: "))
if numero_1 > numero_2 and numero_1 > numero_3:
    print ("El primer número ingresado", numero_1, "es el mayor")
    if numero_1 % 2 == 0:
        print ("y es par.")
    else:
        print ("y es impar.")
if numero_2 > numero_1 and numero_2 > numero_3:
    print ("El segundo número ingresado", numero_2, "es el mayor")
    if numero_2 % 2 == 0:
        print ("y es par.")
    else:
        print ("y es impar.")
if numero_3 > numero_1 and numero_3 > numero_2:
    print ("El tercer número ingresado", numero_2, "es el mayor")
    if numero_3 % 2 == 0:
        print ("y es par.")
    else:
        print ("y es impar.")   
print ("Fin")
