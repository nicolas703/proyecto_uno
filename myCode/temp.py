total = 0
cambioAceiteLux = False
cambioAceiteSimple = False
cambioAceiteReutilizado = False
cambioPastillas1 = False
cambioPastillas2 = False
cambioPastillas3 = False
balanceo1 = False
balanceo2 = False
balanceo3 = False

vehiculo = int(input("Que tipo de vehiculo tiene? \n1. Camioneta \n2. Auto \n3. Moto \nIngrese el número correspondiente a la opcion que desea: "))

print("\nQue pasa mijo que quiere? \nTenemos: \nCambio de aceite \nBalanceo \nCambio de pastillas")

if (vehiculo > 0 and vehiculo < 4):
    cambioAceite = int(input("\nQuiere un cambio de aceite? \n1. SI \n2. NO \nIngrese el número correspondiente a la opcion que desea: "))
    if(cambioAceite == 1):
        tipoAceite = int(input("\nTenemos los siguientes tipos de aceite: \n1. Lux: $15000 \n2. Simple: $10000 \n3. Reutilizado: $7000 \nIngresé el número de la opción que desea: "))
        if(tipoAceite == 1):
            cambioAceiteLux = True
            total += 15000
        elif(tipoAceite == 2):
            cambioAceiteSimple = True
            total += 10000
        elif(tipoAceite == 3):
            cambioAceiteReutilizado = True
            total += 7000
        else:
            print("Ha seleccionado un número inválido, cambio de aceite cancelado")
   
    balanceo = int(input("\nQuiere un balanceo? \n1. SI \n2. NO \nIngrese el número de la opcion que desea: "))
    if(vehiculo == 1):
        balanceo1 = True
        total += 20000
    elif(vehiculo == 2):
        balanceo2 = True
        total += 15000
    else:
        balanceo3 = True
        total += 10000

    cambioPastillas = int(input("\nQuiere un cambio de pastillas? \n1. SI \n2. NO \nIngrese el número de la opcion que desea: "))
    if(vehiculo == 1):
        cambioPastillas1 = True
        total += 25000
    elif(vehiculo == 2):
        cambioPastillas2 = True
        total += 20000
    else:
        cambioPastillas3 = True
        total += 10000
else:
    print("\nHa ingresado un numero de vehiculo inválido, operación cancelada")

print("\n-------- Factura --------\n")

if cambioAceiteLux: print("$15000--Cambio de aceite Lux")
if cambioAceiteSimple: print("$10000--Cambio de aceite Simple")
if cambioAceiteReutilizado: print("$7000---Cambio de aceite Reutilizado")
if balanceo1: print("$20000--Balanceo Camioneta")
if balanceo2: print("$15000--Balanceo Auto")
if balanceo3: print("$10000--Balanceo Moto")
if cambioPastillas1: print("$25000--Cambio de Pastillas Camioneta")
if cambioPastillas2: print("$20000--Cambio de Pastillas Auto")
if cambioPastillas3: print("$10000--Cambio de Pastillas Moto")

print("\nTotal a pagar: $", total)

print("Gracias por preferirnos vuelva pronto")
