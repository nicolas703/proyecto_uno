"""cloro 1 lt 5000
guantes latex 2 pares 1500
spray antibacterial 2500

total > 14990 envio gratis
dentro de la comuna total  9990 envio gratis
dentro comuna 1000
comuna anexa 2000
comuna alejada 5000
"""
# Variable solo referencial
comunaTienda = "Puente Alto"

cloro = 5000
guantes = 1500
spray = 2500

print("Bienvenido a MuereCovid.cl\n Productos disponibles:\n")

print("1. Cloro 1Lt: $5000")
print("2. Guantes de latex, 2 pares: $1500")
print("3. Spray antibacterial: $2500")

print("Ingrese el número del producto que desea comprar:")
producto = int(input())
print("\nIngrese la cantidad unitaria que desea")
cantidad = int(input())

print("\nIngrese la comuna a la que desea enviar su producto")
comunaVenta = input().lower()

delivery = 0
productoAux =0 
productoTotal =0 
total = 0

if(comunaVenta == "la pintana" or comunaVenta == "la florida"):
    delivery = 2000
    if(producto == 1):
        total = cloro * cantidad
        if (total > )

elif(tipoCambio == "USD"):
    cambioFinal = monto * usd
    print("\nUsted  a cambiado: ", tipoCambio, monto,
          "por la siguiente cantidad de Pesos Chilenos: $", cambioFinal)
elif(tipoCambio == "UF"):
    cambioFinal = monto * uf
    print("\nUsted  a cambiado: ", tipoCambio, monto,
          "por la siguiente cantidad de Pesos Chilenos: $", cambioFinal)
elif(tipoCambio == "UTM"):
    cambioFinal = monto * utm
    print("\nUsted  a cambiado: ", tipoCambio, monto,
          "por la siguiente cantidad de Pesos Chilenos: $", cambioFinal)
else:
    print("\nDebe ingresar un tipo de cambio valido(USD, UF o UTM). \n\nEste proceso ha terminado pero puede volver a intetarlo con datos validos")

print("Gracias por preferirnos, vuelva pronto.\n")
