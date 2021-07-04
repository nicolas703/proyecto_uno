from os import system

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

def asientosDisponibles():
    print("A continuación, los asientos disponibles aparecen con su respectivo número.")
    print("Los asientos marcados con una 'X' no se encuentran disponibles.")
    print("Los asientos que tenemos son los siguientes:\n")
    print(f"|   {asientos[1]['asiento']}      {asientos[2]['asiento']}      {asientos[3]['asiento']}                {asientos[4]['asiento']}       {asientos[5]['asiento']}       {asientos[6]['asiento']}    |")
    print(f"|                                                       |")
    print(f"|   {asientos[7]['asiento']}      {asientos[8]['asiento']}      {asientos[9]['asiento']}                {asientos[10]['asiento']}      {asientos[11]['asiento']}      {asientos[12]['asiento']}   |")
    print(f"|                                                       |")
    print(f"|   {asientos[13]['asiento']}     {asientos[14]['asiento']}     {asientos[15]['asiento']}               {asientos[16]['asiento']}      {asientos[17]['asiento']}      {asientos[18]['asiento']}   |")
    print(f"|                                                       |")
    print(f"|   {asientos[19]['asiento']}     {asientos[20]['asiento']}     {asientos[21]['asiento']}               {asientos[22]['asiento']}      {asientos[23]['asiento']}      {asientos[24]['asiento']}   |")
    print(f"|                                                       |")
    print(f"|   {asientos[25]['asiento']}     {asientos[26]['asiento']}     {asientos[27]['asiento']}               {asientos[28]['asiento']}      {asientos[29]['asiento']}      {asientos[30]['asiento']}   |")
    print(f"|   __________________           ____________________   |")
    print(f"|   __________________           ____________________   |")
    print(f"|   {asientos[31]['asiento']}     {asientos[32]['asiento']}     {asientos[33]['asiento']}               {asientos[34]['asiento']}      {asientos[35]['asiento']}      {asientos[36]['asiento']}   |")
    print(f"|                                                       |")
    print(f"|                        VIP                            |")
    print(f"|   {asientos[37]['asiento']}     {asientos[38]['asiento']}     {asientos[39]['asiento']}               {asientos[40]['asiento']}      {asientos[41]['asiento']}      {asientos[42]['asiento']}   |")
    print("\nLos asientos normales (Del 1 al 30) tienen un valor de $78.900 cada uno")
    print("Los asientos VIP (Del 31 al 42) tienen un valor de $240.000 cada uno\n")

def comprarAsiento(asientos, numeroAsiento):
    if asientos[numeroAsiento]['disponibilidad']:
        asientos[numeroAsiento]['asiento'] = 'X' 
        asientos[numeroAsiento]['disponibilidad'] = False
        return({
            "vueloFinal":asientos, 
            "precio": asientos[numeroAsiento]['precio'] 
            })
    else:
        return(False)

def anularPasaje(asientos, numeroAsiento):
    asientos[numeroAsiento]['asiento'] = numeroAsiento 
    asientos[numeroAsiento]['disponibilidad'] = True
    
    return ({
        "asientos":asientos,
        "clientes": clientes 
        })

def crearPax(clientes, nombre, rut, telefono, banco, numeroAsiento):
    if (not clientes.get(numeroAsiento)):
        clientes[numeroAsiento] = {
        "nombre": nombre,
        "rut": rut,
        "telefono": telefono,
        "banco": banco
        }
        return clientes
    else:
        return False

def validaPax(clientes, rut, numeroAsiento):
    asientoRut = clientes.get(numeroAsiento)["rut"] if clientes.get(numeroAsiento) else False 
    return True if asientoRut == rut else False

def cambioDataPax(clientes, numeroAsiento, dato, valor):
    clientes[numeroAsiento][dato] = valor
    return clientes

while(opcion!=5):

    print( bienvenida.center(50, "=") ) 
    print("1. Ver asientos disponibles")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    print("5. Salir")
    #validamos que se permita el ingreso de solo nros
    try:
        opcion=int(input(f"ingrese su opcion \n"))

        if(opcion==1):
            system("cls")
            asientosDisponibles()

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
                    resultado = comprarAsiento(asientos, asiento)

                    asientos = resultado['vueloFinal'] if resultado else print("Este asiento no se encuentra disponible○\n")
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

                telefono = 0
                while(len(telefono) == 8):
                    try:
                        telefono = int(input("\t ingrese un numero de celular 8 digitos\n +569: "))
                    except:
                        print("solo puede ingresar números")


                banco = ""
                while(banco == ""):
                    banco = input("ingrese el nombre de su nombre: ").lower()
                
                resultadoPax = crearPax(clientes, nombre, rut, telefono, banco, asiento)
                clientes = resultadoPax if resultadoPax else print("Este registro no es válido")
                


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

        
