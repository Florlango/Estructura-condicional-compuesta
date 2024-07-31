#Realice un programa que le permita al usuario simular el pago
#ingresando el importe y la forma de pago:
#• Contado (1): se aplica un descuento del 10% al importe
#• Tarjeta (2): se aplica un interés de 10%
#• Débito (3): se aplica un descuento del 5%
#Mostrar el importe, el descuento o interés y el importe total.

monto = float (input("Ingrese el monto a pagar: "))
modo_pago = str ( input("Ingrese modo de pago, contado, crédito o débito: "))
if modo_pago == "contado":
    descuento_contado = monto * 0.1
    precio_contado = monto * 0.8
    print ("El precio de contado es: ", precio_contado, " pesos y el descuento es del", descuento_contado, "pesos.")
elif modo_pago == "crédito" or "credito":
    interes_credito = monto * 0.1
    precio_credito = monto * 1.1
    print ("El precio con tarjeta de crédito es: ", precio_credito , "pesos y el interés es de", interes_credito, "pesos.")
elif modo_pago == "debito" or "débito":
    descuento_debito = monto * 0.05
    precio_debito = monto * 0.95
    print ("El precio con tarjeta de débito es: ", precio_debito, "pesos y el descuento es de", descuento_debito, "pesos.")
print ("Gracias por utilizar nuestros servicios.")
