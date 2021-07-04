from os import system

opcion =0
registros =[]
bienvenida = "Bienvenid@ a Juan Maestro".capitalize()

while(opcion!=4):
    system("cls")
    print( bienvenida.center(50, "=") ) 
    """ print( (50, "Bienvenid@ a Juan Maestro") ) # Centra el mensaje """
    print("1 Registrar Cliente")
    print("2 Suscripcion cliente")
    print("3 Consultar datos cliente")
    print("4 Salir")
    #validamos que se permita el ingreso de solo nros
    try:
        opcion=int(input(f"ingrese su opcion \n"))

        if(opcion==1):
            system("cls")
            print("Registro de clientes")

            run=0
            while(run<5000000 or run >99999999):

                try:
                    run=int(input("\t ingrese su run: "))
                except:
                    print("\tsolo se permiten nros")
                        
            nombre=""
            while(nombre==""):
                nombre=input("\t ingrese nombre del cliente: ")

            direccion=""
            while(direccion==""):
                direccion=input("\t ingrese direccion del cliente: ")

            comuna=""
            while(comuna==""):
                comuna=input("\t ingrese comuna del cliente: ")
                
            # string.find(value, start, end)
            correo=""
            while(correo.find("@")==-1):
                try:
                    correo=input("\t ingrese el correo del cliente: ")
                except:
                    print("\t Debe ingresar su correo en el formato correcto nombre@gmail.com ")
                
            edad = 0
            while(edad >= 10 or edad <= 110):
                try:
                    edad=input("\t ingrese su edad")
                except:
                    print("\tSolo se permiten numeros")
                
            sexo = ""
            sexo = sexo.swapcase()
            while(sexo == "f" or sexo == "m" ):
                sexo = input("\t solo debe ingresar un letra segun su opcion\n F: femenino \n M: masculino \n")
                
                
            celular = 0
            while(len(celular) == 8):
                celular = int(input("\t ingrese un numero de celular 8 digitos\n +569: "))
            
            tipo = ""
            tipo = tipo.upper()
            while(tipo=="PREMIUM" or tipo=="GOLD" or tipo=="SILVER"):
                tipo = input("Escriba el tipo de suscripcion que posee: Premium, Golg, Silver:\n ")
                
            
            diccionario={
                "run":run,
                "nombre":nombre,
                "direccion":direccion,
                "comuna":comuna,
                "correo":correo,
                "edad": edad,
                "sexo":sexo,
                "celular":celular,
                "tipo":tipo
            }

            print("diccionaro")
            print(diccionario)
            registros.append(diccionario)
            print(registros)
            input("presione enter para continuar")


        elif(opcion==2):
            system("cls")
            print("suscripcion de cliente")
        elif(opcion==3):
            system("cls")
            print("consultar datos de cliente")
        elif(opcion==4):
            system("cls")
            print("usted ha salido del sistema")
            print("Gracias por suscribirse a la App de Juan Maestro")
        else:
            system("cls")
            print("Esa opcion no existe")
    except:
        system("cls")
        print("solo se permiten numeros")

        
   