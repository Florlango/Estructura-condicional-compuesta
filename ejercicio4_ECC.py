#Confeccione un programa que pida un número del 1 al 7 y diga el día de
#la semana correspondiente.

diasemana = {1:"Lunes", 
             2:"Martes", 
             3:"Miércoles", 
             4:"Jueves", 
             5:"Viernes", 
             6:"Sábado", 
             7:"Domingo"}
    
numero = int(input("Introduce un número del 1 al 7: "))

if 1<=numero<=7:
    print (f"El día de la semana es: {diasemana[numero]}")

else: print ("El número ingresado no es válido.") 
