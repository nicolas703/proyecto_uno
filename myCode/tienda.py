"""1.	La Tienda MicroPlaying Abrirá una nueva sucursal en Puente Alto, los dueños necesitan conocer a su público y analizar que juegos se compran más esta localidad.

Para conocer el mercado y realizar un acercamiento inicial, se realizará una encuesta.
Para ello se han elegido algunos videojuegos que saldrán a la venta con mayor solicitud en el mercado, para determina, cuál de estos juegos compraría la gente.
Los videojuegos a seleccionar son:

a.	DETROIT precio retiro en tienda $39.990, precio delivery $45.000
b.	DARK SOULS precio retiro en tienda $32.990, precio delivery $40.000
c.	STREET FIGHTER precio retiro en tienda $39.990, precio delivery $45.000
d.	DONKEY KONG precio retiro en tienda $44.990, precio delivery $50.000

La Encuesta deberá tener las siguientes preguntas:
•	Cuál de los 4 juegos prefiere para jugar
•	Del juego escogido, cual de la opciones prefiere Retiro en Tienda o Delivery
•	Cuál de los cuatro juegos no jugaría nunca
Debe generar una aplicación que les pregunte a tres personas de la localidad, la encuesta anteriormente mencionada, y Calcular cual es el juego preferido
(Incluyendo su modalidad de entrega preferida) para Puente Alto
"""

preferido = ""

detroit_Retiro_Votos = 0
dark_Souls_Retiro_Votos = 0
street_Fighter_Retiro_Votos = 0
donkey_Kong_Retiro_Votos = 0

detroit_Delivery_Votos = 0
dark_Souls_Delivery_Votos = 0
street_Fighter_Delivery_Votos = 0
donkey_Kong_Delivery_Votos = 0

print("Es usted residente de la comuna Puente Alto?")
comuna_uno = int(input("Ingrese '1' si su respuesta es SI\nIngrese '2' si su respuesta es NO \n"))

if (comuna_uno == 1):

    print("\nBienvenido a MicroPlaying. \nOfrecemos los siguientes videoJuegos. \nDebe escoger cuál de los 4 juegos prefiere jugar y cual nunca jugaría:")
    print("\n1. DETROIT \n2. DARK SOULS \n3. FIGHTER \n4. DONKEY KONG")

    juego_Uno = int(input("\nIngrese el número del juego que prefiere jugar: "))
    juego_Dos = int(input("\nIngrese el número del juego que nunca jugaría: "))

    if(juego_Uno == 1):
        print("\nHa elegido como juego preferido DETROIT\n Como preferiría la entrega: \n1. precio retiro en tienda $39.990 \n2. precio delivery $45.000 ")
        precio = int(input("\nIngrese el número de su método de entrega preferido : "))
        if(precio == 1):
            detroit_Retiro_Votos = detroit_Retiro_Votos + 1
        elif(precio == 2):
            detroit_Delivery_Votos += 1
        else:
            print("\nHa elegido un número inválido\n\n----- VOTO NULO -----")

    elif(juego_Uno == 2):
        print("\nHa elegido como juego preferido DARK SOULS\n Como preferiría la entrega: \n1. precio retiro en tienda $32.990 \n2. precio delivery $40.000")
        precio = int(input("\nIngrese el número de su método de entrega preferido : "))
        if(precio == 1):
            dark_Souls_Retiro_Votos += 1
        elif(precio == 2):
            dark_Souls_Delivery_Votos += 1
        else:
            print("\nHa elegido un número inválido\n\n----- VOTO NULO -----")

    elif(juego_Uno == 3):
        print("\nHa elegido como juego preferido STREET FIGHTER\n Como preferiría la entrega: \n1. precio retiro en tienda $39.990 \n2. precio delivery $45.000")
        precio = int(input("\nIngrese el número de su método de entrega preferido : "))
        if(precio == 1):
            street_Fighter_Retiro_Votos += 1
        elif(precio == 2):
            street_Fighter_Delivery_Votos += 1
        else:
            print("\nHa elegido un número inválido\n\n----- VOTO NULO -----")

    elif(juego_Uno == 4):
        print("\nHa elegido como juego preferido DONKEY KONG\n Como preferiría la entrega: \n1. precio retiro en tienda $44.990 \n2. precio delivery $50.000 ")
        precio = int(
            input("\nIngrese el número de su método de entrega preferido : "))
        if(precio == 1):
            donkey_Kong_Retiro_Votos += 1
        elif(precio == 2):
            donkey_Kong_Delivery_Votos += 1
        else:
            print("\nHa elegido un número inválido\n\n----- VOTO NULO -----")

    else:
        print("\nHa elegido un número inválido\n\n----- VOTO NULO -----")

    print("\n_______________________________________ \nVoto registrado \n_______________________________________\n")

else:
    print("Gracias por su tiempo, su participación ha sido registrada")

print("\nNuevo voto:\n")

print("Es usted residente de la comuna Puente Alto?")
comuna_dos = int(input("Ingrese '1' si su respuesta es SI\nIngrese '2' si su respuesta es NO \n"))

if (comuna_dos == 1):

    print("\nBienvenido a MicroPlaying. \nOfrecemos los siguientes videoJuegos. \nDebe escoger cuál de los 4 juegos prefiere jugar y cual nunca jugaría:")
    print("\n1. DETROIT \n2. DARK SOULS \n3. FIGHTER \n4. DONKEY KONG")

    juego_Uno = int(input("\nIngrese el número del juego que prefiere jugar: "))
    juego_Dos = int(input("\nIngrese el número del juego que nunca jugaría: "))

    if(juego_Uno == 1):
        print("\nHa elegido como juego preferido DETROIT\n Como preferiría la entrega: \n1. precio retiro en tienda $39.990 \n2. precio delivery $45.000 ")
        precio = int(input("\nIngrese el número de su método de entrega preferido : "))
        if(precio == 1):
            detroit_Retiro_Votos = detroit_Retiro_Votos + 1
        elif(precio == 2):
            detroit_Delivery_Votos += 1
        else:
            print("\nHa elegido un número inválido\n\n----- VOTO NULO -----")

    elif(juego_Uno == 2):
        print("\nHa elegido como juego preferido DARK SOULS\n Como preferiría la entrega: \n1. precio retiro en tienda $32.990 \n2. precio delivery $40.000")
        precio = int(input("\nIngrese el número de su método de entrega preferido : "))
        if(precio == 1):
            dark_Souls_Retiro_Votos += 1
        elif(precio == 2):
            dark_Souls_Delivery_Votos += 1
        else:
            print("\nHa elegido un número inválido\n\n----- VOTO NULO -----")

    elif(juego_Uno == 3):
        print("\nHa elegido como juego preferido STREET FIGHTER\n Como preferiría la entrega: \n1. precio retiro en tienda $39.990 \n2. precio delivery $45.000")
        precio = int(input("\nIngrese el número de su método de entrega preferido : "))
        if(precio == 1):
            street_Fighter_Retiro_Votos += 1
        elif(precio == 2):
            street_Fighter_Delivery_Votos += 1
        else:
            print("\nHa elegido un número inválido\n\n----- VOTO NULO -----")

    elif(juego_Uno == 4):
        print("\nHa elegido como juego preferido DONKEY KONG\n Como preferiría la entrega: \n1. precio retiro en tienda $44.990 \n2. precio delivery $50.000 ")
        precio = int(
            input("\nIngrese el número de su método de entrega preferido : "))
        if(precio == 1):
            donkey_Kong_Retiro_Votos += 1
        elif(precio == 2):
            donkey_Kong_Delivery_Votos += 1
        else:
            print("\nHa elegido un número inválido\n\n----- VOTO NULO -----")

    else:
        print("\nHa elegido un número inválido\n\n----- VOTO NULO -----")

    print("\n_______________________________________ \nVoto registrado \n_______________________________________\n")

else:
    print("Gracias por su tiempo, su participación ha sido registrada")

print("\nNuevo voto:\n")

print("Es usted residente de la comuna Puente Alto?")
comuna_tres = int(input("Ingrese '1' si su respuesta es SI\nIngrese '2' si su respuesta es NO \n"))

if (comuna_tres == 1):

    print("\nBienvenido a MicroPlaying. \nOfrecemos los siguientes videoJuegos. \nDebe escoger cuál de los 4 juegos prefiere jugar y cual nunca jugaría:")
    print("\n1. DETROIT \n2. DARK SOULS \n3. FIGHTER \n4. DONKEY KONG")

    juego_Uno = int(input("\nIngrese el número del juego que prefiere jugar: "))
    juego_Dos = int(input("\nIngrese el número del juego que nunca jugaría: "))

    if(juego_Uno == 1):
        print("\nHa elegido como juego preferido DETROIT\n Como preferiría la entrega: \n1. precio retiro en tienda $39.990 \n2. precio delivery $45.000 ")
        precio = int(input("\nIngrese el número de su método de entrega preferido : "))
        if(precio == 1):
            detroit_Retiro_Votos = detroit_Retiro_Votos + 1
        elif(precio == 2):
            detroit_Delivery_Votos += 1
        else:
            print("\nHa elegido un número inválido\n\n----- VOTO NULO -----")

    elif(juego_Uno == 2):
        print("\nHa elegido como juego preferido DARK SOULS\n Como preferiría la entrega: \n1. precio retiro en tienda $32.990 \n2. precio delivery $40.000")
        precio = int(input("\nIngrese el número de su método de entrega preferido : "))
        if(precio == 1):
            dark_Souls_Retiro_Votos += 1
        elif(precio == 2):
            dark_Souls_Delivery_Votos += 1
        else:
            print("\nHa elegido un número inválido\n\n----- VOTO NULO -----")

    elif(juego_Uno == 3):
        print("\nHa elegido como juego preferido STREET FIGHTER\n Como preferiría la entrega: \n1. precio retiro en tienda $39.990 \n2. precio delivery $45.000")
        precio = int(input("\nIngrese el número de su método de entrega preferido : "))
        if(precio == 1):
            street_Fighter_Retiro_Votos += 1
        elif(precio == 2):
            street_Fighter_Delivery_Votos += 1
        else:
            print("\nHa elegido un número inválido\n\n----- VOTO NULO -----")

    elif(juego_Uno == 4):
        print("\nHa elegido como juego preferido DONKEY KONG\n Como preferiría la entrega: \n1. precio retiro en tienda $44.990 \n2. precio delivery $50.000 ")
        precio = int(
            input("\nIngrese el número de su método de entrega preferido : "))
        if(precio == 1):
            donkey_Kong_Retiro_Votos += 1
        elif(precio == 2):
            donkey_Kong_Delivery_Votos += 1
        else:
            print("\nHa elegido un número inválido\n\n----- VOTO NULO -----")

    else:
        print("\nHa elegido un número inválido\n\n----- VOTO NULO -----")

    print("\n_______________________________________ \nVoto registrado \n_______________________________________\n")

else:
    print("Gracias por su tiempo, su participación ha sido registrada")


if(detroit_Retiro_Votos > dark_Souls_Retiro_Votos and detroit_Retiro_Votos > street_Fighter_Retiro_Votos):
    preferido = "El juego favorito es: detroit con retiro en tienda"

"detroit_Retiro_Votos"
"dark_Souls_Retiro_Votos"
"street_Fighter_Retiro_Votos"
"donkey_Kong_Retiro_Votos"

"detroit_Delivery_Votos"
"dark_Souls_Delivery_Votos"
"street_Fighter_Delivery_Votos"
"donkey_Kong_Delivery_Votos"

print(preferido)