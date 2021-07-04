nota1 = float(input("Ingrese su primera nota\n"))
nota2 = float(input("Ingrese su segunda nota\n"))
nota3 = float(input("Ingrese su tercera nota\n"))

if(nota1 < 1.0 or nota2 < 1.0 or nota3 < 1.0 or nota1 > 7.0 or nota2 > 7.0 or nota3 > 7.0):
    print("\nDebe ingresar notas validas(Entre 1.0 y 7.0))")
else:
    promedio = (nota1+nota2+nota3) / 3
    print("Su promedio es: ", promedio)
    if(promedio==7.0):
        print("Usted se ha ganado 1 kilo de frugele por bakan ;)")
    elif(promedio>=6.0):
        print("Eso eso!!")
    elif(promedio>=4.0):
        print("Vamos que se puede")
    else:
        print("A ponerse a estudiar")