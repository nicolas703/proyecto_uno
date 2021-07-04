from math import pi

def areaCirculo():
    radio = float(input("Ingrese el radio de el círculo: "))
    area = pi * radio**2
    return(round(area,3))    
    


def perimetroCuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    perimetro = lado *4
    return (perimetro)

def esPalindromo(frase):
    frase = frase.lowercase()
    frase = frase.replaace (" ", "")
    
    
def esPalindromo(texto): return True if texto[::-1].replace(" ", "") == texto.replace(" ", "") else False


def relacion(a,b):
        if(a>b):
            return("1")
        elif(a<b):
            return("-1")
        else:
            return("0")
        
def verificar(arreglo):
    try:
        numero = int(input("Ingrese un número :"))
        if numero in arreglo:
            return("El número pertenece a la lista")
        else:
            return("El número no pertenece a la lista")
    except:
        return("Solo numeros") 
    

def asientosDisponibles(asientos):
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
        asientos[numeroAsiento]['asiento'] = 'X' if numeroAsiento < 10 else 'X '
        asientos[numeroAsiento]['disponibilidad'] = False
        return({
            "vueloFinal":asientos, 
            "precio": asientos[numeroAsiento]['precio'] 
            })
    else:
        return(False)

def anularPasaje(asientos, numeroAsiento,clientes):
    asientos[numeroAsiento]['asiento'] = numeroAsiento 
    asientos[numeroAsiento]['disponibilidad'] = True
    clientes.pop(numeroAsiento)
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


def promedio(array):
    promedios = []
    for columna in range(len(array[0])):
        suma = 0
        for fila in range(len(array)):
            suma += array[fila][columna]
        promedios.append(suma/len(array))
    return promedios
