from os import system

import random

def validaCorreo(correo):
    arroba = correo.find("@")

    if arroba != -1:
            return correo
    else:
        return False


opcion = 0
registroCliente = []
system("cls")
while(opcion != 4):

    print("\tMenu Calera de tango net")
    print("1.     Registrar cliente ")
    print("2.     Descontar Mb")
    print("3.     Consultar datos de un cliente")
    print("4.     Salir")

    try:
        opcion = int(input("ingrese su opcion "))
        if (opcion == 1):
            system("cls")
            print("\tRegistrar cliente")

            codigo = random.randint(5000, 150000)

            run = 0
            ''' Rut, no se debe validar el dígito verificador,
            solo que la parte numérica sea efectivamente numérica y que esté en el rango de 1 y 99.999.999  '''
            while(run < 3000000 or run > 99999999):
                try:
                    run = int(
                        input("Ingrese su número de run, sin el dígito verificador: "))
                except:
                    print("solo puede ingresar números")

            nombre = ""
            while(nombre == ""):
                nombre = input("ingrese el nombre del cliente: ")

            apellido = ""
            while(apellido == ""):
                apellido = input("ingrese el apellido del cliente: ")

            edad = 0
            while(edad < 15 or edad > 110):
                try:
                    edad = int(input("Ingrese su edad: "))
                    if edad < 15 or edad > 110:
                        print(
                            "Debe tener entre 15 y 110 años para poder continuar con el proceso de registro")
                except:
                    print("solo puede ingresar números")

            sexo = ""
            while(sexo != "f" and sexo != "m"):
                sexo = input("Ingrese su sexo \nSolo se permite \"F\" (femenino) y \"M\" (Masculino):\n ").lower()
                if sexo != "f" and sexo != "m":
                    print("Debe ingresar un dato válido")
                
            correo = ""
            while(not correo):
                correo = input("ingrese el correo: ")
                correo = validaCorreo(correo)
                if not correo:
                    print("Debe ingresar un correo valido")

            plan = ""
            while(plan != "estudiante" and plan != "feliz" and plan != "empresario"):
                plan = input("Ingrese el nombre del plan que desea contratar(estudiante, empresario o feliz): ").lower()
                if plan != "estudiante" and plan != "feliz" and plan != "empresario":
                    print("Debe ingresar un nombre de plan valido")

            cantidadMb = 10000

            cliente = {
                "codigo": codigo,
                "run": run,
                "nombre": nombre,
                "apellido": apellido,
                "edad": edad,
                "sexo": sexo,
                "plan": plan,
                "correo": correo,
                "cantidadMb": cantidadMb
            }

            registroCliente.append(cliente)

        elif (opcion==2):
            system("cls")
            print("Descontar Mb")
            
            runEncontrado = True
            runABuscar=0                
            while(runABuscar <3000000 or run >99999999 or runEncontrado):
                try:
                    runABuscar=int(input("ingrese el numero de run, sin dígito verificador: "))
                except:
                    print("solo puede ingresar un nro")

                for datoGuardado in registroCliente:
                    runGuardado=datoGuardado.get("run")
                    bandera=True
                    if runGuardado==runABuscar:
                        cantidadMbArestar=""
                        while(cantidadMbArestar==""):
                            try:
                                cantidadMbArestar=int(input("Ingrese la cantidad de Mb que desea descontar: "))

                                if cantidadMbArestar > datoGuardado.get("cantidadMb") :
                                    print("Debe ingresar un número menor a ", datoGuardado.get("cantidadMb"))
                                    bandera=False
                                else :
                                    bandera=True
                                if not bandera:
                                    cantidadMbArestar=""
                            except:
                                print("Solo números")
                        datoGuardado["cantidadMb"]-=cantidadMbArestar
                        runEncontrado = False
                    else:
                        print("No existen registros para este run")   
 

        elif (opcion==3):
            system("cls")
            print("Consultar datos de un cliente ")
            runABuscar=0                
            runEncontrado = True
            while(runABuscar <3000000 or run >99999999 or runEncontrado):
                try:
                    runABuscar=int(input("ingrese el numero de run, sin dígito verificador: "))
                except:
                    print("solo puede ingresar un nro")
            
                for datoGuardado in registroCliente:
                        
                    runGuardado=datoGuardado.get("run")
                    if runGuardado==runABuscar:

                        codigo=datoGuardado.get("codigo")
                        run=datoGuardado.get("run")
                        nombre=datoGuardado.get("nombre")
                        apellido=datoGuardado.get("apellido")
                        edad=datoGuardado.get("edad")
                        sexo=datoGuardado.get("sexo")
                        plan=datoGuardado.get("plan")
                        correo=datoGuardado.get("correo")
                        cantidadMb=datoGuardado.get("cantidadMb")

                        print("Datos del cliente buscado:")
                        print(f"codigo: {codigo}")
                        print(f"run: {run}")
                        print(f"nombre :{nombre}")
                        print(f"apellido : {apellido}")
                        print(f"edad : {edad}")
                        print(f"sexo : {sexo}")
                        print(f"plan : {plan}")
                        print(f"correo: {correo}")
                        print(f"Mb : {cantidadMb}")
                        runEncontrado = False
                        break
                    else:
                        runEncontrado = True
                        print("No existen registros para este run")   



        elif (opcion==4):
            system("cls")
            print("Gracias por preferir CaleraDeTango.net")
            print("Vuelva pronto")
        
        else:
            print("esa opcion no existe ")
    except:
        system("cls")
        print("solo puede ingresar un nro")


