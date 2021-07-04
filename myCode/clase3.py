usd = 718
uf = 28123
utm = 51325

print("Casa de cambio Online ofrece los siguientes tipos de cambio:\n")
print("1. USD => Pesos Chilenos \n2. UF => Pesos Chilenos \n3. UTM => Pesos Chilenos\n")

print("Ingrese la moneda que desea convertir a Pesos Chilenos: USD, UF o UTM")

tipoCambio = input().upper()

monto = int(input("\nIngrese la cantidad que desea convertir:"))

if(monto < 0):
    print("Debe ingresar un monto mayor a 0 para realizar un cambio valido. \nEste proceso ha terminado pero puede volver a intetarlo con datos validos")
elif(tipoCambio == "USD"):
    cambioFinal =  monto * usd
    print("\nUsted  a cambiado: ", tipoCambio, monto, "por la siguiente cantidad de Pesos Chilenos: $", cambioFinal)
elif(tipoCambio == "UF"):
    cambioFinal = monto * uf
    print("\nUsted  a cambiado: ", tipoCambio, monto, "por la siguiente cantidad de Pesos Chilenos: $", cambioFinal)
elif(tipoCambio == "UTM"):
    cambioFinal = monto * utm
    print("\nUsted  a cambiado: ", tipoCambio, monto, "por la siguiente cantidad de Pesos Chilenos: $", cambioFinal)
else:
    print("\nDebe ingresar un tipo de cambio valido(USD, UF o UTM). \n\nEste proceso ha terminado pero puede volver a intetarlo con datos validos")

print("Gracias por preferirnos, vuelva pronto.\n")