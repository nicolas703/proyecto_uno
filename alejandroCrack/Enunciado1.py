from os import system
import util as ut
opcion = 0
bienvenida = "Bienvenid@ a Vuelos-Duoc".capitalize()

valorNormal = 78900
valorVip = 240000
asientos = {
    1: {
        "asiento": "1",
        "disponibilidad": True,
        "precio": valorNormal
    },
    2: {
        "asiento": "2",
        "disponibilidad": True,
        "precio": valorNormal
    },
    3: {
        "asiento": "3",
        "disponibilidad": True,
        "precio": valorNormal
    },
    4: {
        "asiento": "4",
        "disponibilidad": True,
        "precio": valorNormal
    },
    5: {
        "asiento": "5",
        "disponibilidad": True,
        "precio": valorNormal
    },
    6: {
        "asiento": "6",
        "disponibilidad": True,
        "precio": valorNormal
    },
    7: {
        "asiento": "7",
        "disponibilidad": True,
        "precio": valorNormal
    },
    8: {
        "asiento": "8",
        "disponibilidad": True,
        "precio": valorNormal
    },
    9: {
        "asiento": "9",
        "disponibilidad": True,
        "precio": valorNormal
    },
    10: {
        "asiento": "10",
        "disponibilidad": True,
        "precio": valorNormal
    },
    11: {
        "asiento": "11",
        "disponibilidad": True,
        "precio": valorNormal
    },
    12: {
        "asiento": "12",
        "disponibilidad": True,
        "precio": valorNormal
    },
    13: {
        "asiento": "13",
        "disponibilidad": True,
        "precio": valorNormal
    },
    14: {
        "asiento": "14",
        "disponibilidad": True,
        "precio": valorNormal
    },
    15: {
        "asiento": "15",
        "disponibilidad": True,
        "precio": valorNormal
    },
    16: {
        "asiento": "16",
        "disponibilidad": True,
        "precio": valorNormal
    },
    17: {
        "asiento": "17",
        "disponibilidad": True,
        "precio": valorNormal
    },
    18: {
        "asiento": "18",
        "disponibilidad": True,
        "precio": valorNormal
    },
    19: {
        "asiento": "19",
        "disponibilidad": True,
        "precio": valorNormal
    },
    20: {
        "asiento": "20",
        "disponibilidad": True,
        "precio": valorNormal
    },
    21: {
        "asiento": "21",
        "disponibilidad": True,
        "precio": valorNormal
    },
    22: {
        "asiento": "22",
        "disponibilidad": True,
        "precio": valorNormal
    },
    23: {
        "asiento": "23",
        "disponibilidad": True,
        "precio": valorNormal
    },
    24: {
        "asiento": "24",
        "disponibilidad": True,
        "precio": valorNormal
    },
    25: {
        "asiento": "25",
        "disponibilidad": True,
        "precio": valorNormal
    },
    26: {
        "asiento": "26",
        "disponibilidad": True,
        "precio": valorNormal
    },
    27: {
        "asiento": "27",
        "disponibilidad": True,
        "precio": valorNormal
    },
    28: {
        "asiento": "28",
        "disponibilidad": True,
        "precio": valorNormal
    },
    29: {
        "asiento": "29",
        "disponibilidad": True,
        "precio": valorNormal
    },
    30: {
        "asiento": "30",
        "disponibilidad": True,
        "precio": valorNormal
    },
    31: {
        "asiento": "31",
        "disponibilidad": True,
        "precio": valorVip
    },
    32: {
        "asiento": "32",
        "disponibilidad": True,
        "precio": valorVip
    },
    33: {
        "asiento": "33",
        "disponibilidad": True,
        "precio": valorVip
    },
    34: {
        "asiento": "34",
        "disponibilidad": True,
        "precio": valorVip
    },
    35: {
        "asiento": "35",
        "disponibilidad": True,
        "precio": valorVip
    },
    36: {
        "asiento": "36",
        "disponibilidad": True,
        "precio": valorVip
    },
    37: {
        "asiento": "37",
        "disponibilidad": True,
        "precio": valorVip
    },
    38: {
        "asiento": "38",
        "disponibilidad": True,
        "precio": valorVip
    },
    39: {
        "asiento": "39",
        "disponibilidad": True,
        "precio": valorVip
    },
    40: {
        "asiento": "40",
        "disponibilidad": True,
        "precio": valorVip
    },
    41: {
        "asiento": "41",
        "disponibilidad": True,
        "precio": valorVip
    },
    42: {
        "asiento": "42",
        "disponibilidad": True,
        "precio": valorVip
    }
}
clientes = {}

while(opcion!=5):

    print( bienvenida.center(50, "=") ) 
    print("1. Ver asientos disponibles")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    print("5. Salir")
    
    try:
        opcion=int(input(f"ingrese su opcion \n"))

        if(opcion==1):
            system("cls")
            ut.asientosDisponibles(asientos)

        elif(opcion==2):
            system("cls")
            print("Por favor Ingrese los siguientes datos para realizar una compra: ")
            valorSinDescuento = 0
            asiento = -1
            asientoValido = False
            while (asiento < 1 or asiento > 42 or not asientoValido):
                try:
                    print("IMPORTANTE: \nSi no ha revisado los asientos disponibles para elegir uno, ingrese el número 0 en lugar de un número de asiento")
                    print("y volverá al menú principal para elegir la opción 1. Ver vuelos disponibles. \n")

                    asiento = int(input("Ingrese el número de asiento a comprar: "))
                    resultado = ut.comprarAsiento(asientos, asiento)
                    asientos = resultado['vueloFinal'] if resultado else asientos 
                    if not resultado: print("Este asiento no se encuentra disponible\n")
                    valorSinDescuento = resultado['precio'] if resultado else 0
                    asientoValido = True if resultado else False
                except:
                    print("solo puede ingresar números")

                if asiento == 0:
                    break

            if asiento != 0:                
                nombre = ""
                while(nombre == ""):
                    nombre = input("ingrese su nombre: ")

                rut = 0
                
                while(rut < 3000000 or rut > 999999999):
                    try:
                        rut = int(input("Ingrese su número de rut, sin el dígito verificador: "))
                    except:
                        print("solo puede ingresar números")

                telefono =0
                while(len(str(telefono))!=8):
                    try:
                        telefono = int(input("Ingrese un numero de celular 8 digitos\n +569: "))      
                    except:
                        print("Solo se permiten numeros")

                banco = ""
                while(banco == ""):
                    banco = input("ingrese el nombre de su banco: ").lower()
                
                resultadoPax = ut.crearPax(clientes, nombre, rut, telefono, banco, asiento)
                clientes = resultadoPax if resultadoPax else print("Este registro no es válido")
                precio = valorSinDescuento*0.85 if (banco=="bancoduoc") else valorSinDescuento
                print(f"Su total a pagar es: ${precio}")

        elif(opcion==3):
            system("cls")
            print("Anular vuelo")
            rut = 0
            asiento = 0    
            while(rut < 3000000 or rut > 999999999):
                try:
                    rut = int(input("Ingrese su número de rut, sin el dígito verificador: "))
                except:
                    print("solo puede ingresar números")
            while (asiento < 1 or asiento > 42):
                try:       
                    asiento = int(input("Ingrese el número de asiento a anular: "))
                except:
                    print("Sólo se aceptan numeros")
                    
            resultado = ut.validaPax(clientes,rut,asiento)
            if (resultado):
                anulacion = ut.anularPasaje(asientos,asiento,clientes) 
                asientos = anulacion["asientos"]
                clientes = anulacion["clientes"]  
                print("Reserva anulada correctamente")               
            else:
                print("Los datos no corresponden a la reserva")
                
        elif(opcion==4):
            system("cls")
            print("Modificar datos del pasajero")
            rut = 0
            asiento = 0    
            while(rut < 3000000 or rut > 999999999):
                try:
                    rut = int(input("Ingrese su número de rut, sin el dígito verificador: "))
                except:
                    print("solo puede ingresar números")
            while (asiento < 1 or asiento > 42):
                try:       
                    asiento = int(input("Ingrese el número de asiento a modificar: "))
                except:
                    print("Sólo se aceptan numeros")
                    
            resultado = ut.validaPax(clientes,rut,asiento)
            if (resultado):
               while(opcion !=3):
        
                    print("\tElija el dato a cambiar: ")
                    print("1) Nombre pasajero")
                    print("2) Telefono pasajero")
                    print("3) Volver al menú principal")
                    try:
                        opcion = int (input("Ingrese una de las opciones: "))
         
                        if(opcion ==1):
                            nombre = ""
                            while(nombre == ""):
                                nombre = input("ingrese su nombre: ")
                                
                            actualizacionCliente = ut.cambioDataPax(clientes,asiento,"nombre",nombre)
                            print("Nombre actualizado correctamente") 
                             
                        elif(opcion ==2):
                            telefono =0
                            while(len(str(telefono))!=8):
                                try:
                                    telefono = int(input("Ingrese un numero de celular 8 digitos\n +569: "))      
                                except:
                                    print("Solo se permiten numeros")
                            
                            actualizacionCliente = ut.cambioDataPax(clientes,asiento,"telefono",telefono)
                            print("Telefono actualizado correctamente") 
                                
                        elif(opcion ==3):
                            print("Volverás al menú principal")
                            
                        else:
                            print("Esa opción no existe")
                            
                    except:
                        print("Sólo se aceptan números")        
                                           
            else:
                print("Los datos no corresponden a la reserva")
            
        elif(opcion==5):
            system("cls")
            print("!Gracias por preferirnos!\nVuelva pronto.")
        else:
            system("cls")
            print("Esa opcion no existe")
    except:
        system("cls")
        print("solo se permiten numeros")

        
