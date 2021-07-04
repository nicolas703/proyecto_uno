menu_comida = {
    "completo": 1000,
    "churrasco": 1500,
    "papas_fritas": 1250
}

menu_bebestibles = {
    "jugo": 750,
    "bebidas": 500,
    "agua_mineral": 400
}

comida = 0
cantidad_comida = 0
bebida = 0
cantidad_bebida = 0
cliente = 0


def menu():
    print("Bienvenido a peor es na")

    print("Nuestro menú en comidas es:")
    print("1. Completo:     $1000")
    print("2. Churrasco:    $1500")
    print("3. Papas Fritas: $1250")
    print("si no desea ningún producto ingrese 4")

    global comida 
    comida = int(input("Ingrese el número de la comida comprará:"))
    global cantidad_comida 
    cantidad_comida = int(input("Ingrese la cantidad que desea comprar:"))

    print("Nuestro menú en bebestibles es:")
    print("1. Jugo:         $750")
    print("2. Bebida:       $500")
    print("3. Agua Mineral: $400")
    print("si no desea ningún producto ingrese 4")

    global bebida
    bebida = int(input("Ingrese el número de la bebida comprará:"))
    global cantidad_bebida
    cantidad_bebida = int(input("Ingrese la cantidad que desea comprar:"))

    print("Es cliente frecuente?")
    print("1. Si")
    print("2. No")

    global cliente
    cliente = int(input("Ingrese el número de cliente:"))


def compra(bebida, comida, cliente):
    if comida == 1:
        total_comida = menu_comida["completo"] * cantidad_comida
        print("Total por alimentos: $", total_comida)
    elif comida == 2:
        total_comida = menu_comida["churrasco"] * cantidad_comida
        print("Total por alimentos: $", total_comida)
    elif comida == 3:
        total_comida = menu_comida["papas_fritas"] * cantidad_comida
        print("Total por alimentos: $", total_comida)
    else:
        total_comida = 0
        print("Total por alimentos: $", total_comida)

    if bebida == 1:
        total_bebida = menu_bebestibles["jugo"] * cantidad_bebida
        print("Total por bebidas: $", total_bebida)
    elif bebida == 2:
        total_bebida = menu_bebestibles["bebidas"] * cantidad_bebida
        print("Total por bebidas: $", total_bebida)
    elif bebida == 3:
        total_bebida = menu_bebestibles["agua_mineral"] * cantidad_bebida
        print("Total por bebidas: $", total_bebida)
    else:
        total_bebida = 0
        print("Total por bebidas: $", total_bebida)

    sub_total = total_comida + total_bebida
    print("Subtotal: $", sub_total)

    if cliente == 1:
        total = sub_total * 0.9
    else:
        total = sub_total

    print("Total: $", total)
    print("Gracias por comprar en peor es na, disfrute su comida y vuelva pronto")

def init():
    menu()
    print(comida)
    while comida > 4 or comida < 1 or bebida > 4 or bebida < 1 or cliente > 2 or cliente < 1:
        if comida > 3 or comida < 1:
            print("------ERROR-----")
            print("Debe ingresar un número valido al pedir comida")
            print("----------------")
            menu()
        elif bebida > 3 or bebida < 1:
            print("------ERROR-----")
            print("Debe ingresar un número valido al pedir bebida")
            print("----------------")
            menu()
        elif cliente >= 3 or cliente <= 0:
            print("------ERROR-----")
            print("Debe ingresar un número valido al ingresar el tipo de cliente")
            print("----------------")
            menu()

    compra(bebida, comida, cliente)

init()
