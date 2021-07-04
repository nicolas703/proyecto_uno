valor_categoria=0
descuento=0
valorfinal=0
pastor=int(input("Ingrese un numero según que tipo de pastor es:\n1)Pastor Vaca\n2)Pastor Oveja\n3)Pastor Murcielago\n4)Pastor Chancho\n5)Otro tipo de pastor\nIngrese su opcion aqui-----> "))
if  (pastor==1 or pastor==2 or pastor==3 or pastor==4 or pastor==5):
    print("-------Nesfis-------\nLux)15000\nAmpliado)10000\nBasico)7000\n-------Dinei-------\nLux)20000\nAmpliado)15000\nBasico)10000\n-------Statsr-------\nLux)25000\nAmpliado)20000\nBasico)10000\n")
    servicio=int(input("Seleccione que servicio desea contratar escribiendo el numero que corresponde a cada uno:\n1)Nesfis\n2)Dinei\n3)Statsr\nEscriba aqui su respuesta---> "))
    if (servicio==1 or servicio==2 or servicio==3):
        categoria=int(input("Ingrese que tipo de tarifa desea contratar:\n1)Lux\n2)Ampliado\n3)Basico\nEscriba su respuesta aqui---> "))
#---------------------------------------------Nesfis-----------------------------
        if(servicio==1 and categoria==1):
            valor_categoria= valor_categoria +15000
            if (pastor==1):
                descuento=(valor_categoria*17)/100
                valorfinal=valor_categoria-descuento
            if (pastor==2):
                descuento=(valor_categoria*5)/100
                valorfinal=valor_categoria-descuento
            if  (pastor==3):
                descuento=(valor_categoria*23)/100
                valorfinal=valor_categoria-descuento
            if (pastor==4):
                descuento=(valor_categoria*4)/100
                valorfinal=valor_categoria-descuento
            print(f"Usted ah seleccionado El servicio Nesfis y la categoria Lux, Debe pagar {valorfinal}")
        if(servicio==1 and categoria==2):
            valor_categoria = valor_categoria +10000
            if (pastor==1):
                descuento=(valor_categoria*17)/100
                valorfinal=valor_categoria-descuento
            if (pastor==2):
                descuento=(valor_categoria*5)/100
                valorfinal=valor_categoria-descuento
            if  (pastor==3):
                descuento=(valor_categoria*23)/100
                valorfinal=valor_categoria-descuento
            if (pastor==4):
                descuento=(valor_categoria*4)/100
                valorfinal=valor_categoria-descuento
            print(f"Usted ah seleccionado El servicio Nesfis y la categoria Ampliado, Debe pagar {valorfinal}")
        if(servicio==1 and categoria==3):
            valor_categoria= valor_categoria +7000
            if (pastor==1):
                descuento=(valor_categoria*17)/100
                valorfinal=valor_categoria-descuento
            if (pastor==2):
                descuento=(valor_categoria*5)/100
                valorfinal=valor_categoria-descuento
            if  (pastor==3):
                descuento=(valor_categoria*23)/100
                valorfinal=valor_categoria-descuento
            if (pastor==4):
                descuento=(valor_categoria*4)/100
                valorfinal=valor_categoria-descuento
                print(f"Usted ah seleccionado El servicio Nesfis y la categoria Basico, Debe pagar {valorfinal}")
#---------------------------------------------Dinei-----------------------------
        if(servicio==2 and categoria==1):
            valor_categoria= valor_categoria +20000
            if (pastor==1):
                descuento=(valor_categoria*17)/100
                valorfinal=valor_categoria-descuento
            if (pastor==2):
                descuento=(valor_categoria*5)/100
                valorfinal=valor_categoria-descuento
            if  (pastor==3):
                descuento=(valor_categoria*23)/100
                valorfinal=valor_categoria-descuento
            if (pastor==4):
                descuento=(valor_categoria*4)/100
                valorfinal=valor_categoria-descuento
            print(f"Usted ah seleccionado El servicio Dinei y la categoria Lux, Debe pagar {valorfinal}")
        if(servicio==2 and categoria==2):
            valor_categoria = valor_categoria +15000
            if (pastor==1):
                descuento=(valor_categoria*17)/100
                valorfinal=valor_categoria-descuento
            if (pastor==2):
                descuento=(valor_categoria*5)/100
                valorfinal=valor_categoria-descuento
            if  (pastor==3):
                descuento=(valor_categoria*23)/100
                valorfinal=valor_categoria-descuento
            if (pastor==4):
                descuento=(valor_categoria*4)/100
                valorfinal=valor_categoria-descuento
            print(f"Usted ah seleccionado El servicio Dinei y la categoria Ampliado, Debe pagar {valorfinal}")
        if(servicio==2 and categoria==3):
            valor_categoria= valor_categoria +10000
            if (pastor==1):
                descuento=(valor_categoria*17)/100
                valorfinal=valor_categoria-descuento
            if (pastor==2):
                descuento=(valor_categoria*5)/100
                valorfinal=valor_categoria-descuento
            if  (pastor==3):
                descuento=(valor_categoria*23)/100
                valorfinal=valor_categoria-descuento
            if (pastor==4):
                descuento=(valor_categoria*4)/100
                valorfinal=valor_categoria-descuento
            print(f"Usted ah seleccionado El servicio Dinei y la categoria Basico, Debe pagar {valorfinal}")
#---------------------------------------------Statsr-----------------------------
        if(servicio==3 and categoria==1):
            valor_categoria= valor_categoria +25000
            if (pastor==1):
                descuento=(valor_categoria*17)/100
                valorfinal=valor_categoria-descuento
            if (pastor==2):
                descuento=(valor_categoria*5)/100
                valorfinal=valor_categoria-descuento
            if  (pastor==3):
                descuento=(valor_categoria*23)/100
                valorfinal=valor_categoria-descuento
            if (pastor==4):
                descuento=(valor_categoria*4)/100
                valorfinal=valor_categoria-descuento
            print(f"Usted ah seleccionado El servicio Statsr y la categoria Lux, Debe pagar {valorfinal}")
        if(servicio==3 and categoria==2):
            valor_categoria = valor_categoria +20000
            if (pastor==1):
                descuento=(valor_categoria*17)/100
                valorfinal=valor_categoria-descuento
            if (pastor==2):
                descuento=(valor_categoria*5)/100
                valorfinal=valor_categoria-descuento
            if  (pastor==3):
                descuento=(valor_categoria*23)/100
                valorfinal=valor_categoria-descuento
            if (pastor==4):
                descuento=(valor_categoria*4)/100
                valorfinal=valor_categoria-descuento
            print(f"Usted ah seleccionado El servicio Statsr y la categoria Ampliado, Debe pagar {valorfinal}")
        if(servicio==3 and categoria==3):
            valor_categoria= valor_categoria +10000
            if (pastor==1):
                descuento=(valor_categoria*17)/100
                valorfinal=valor_categoria-descuento
            if (pastor==2):
                descuento=(valor_categoria*5)/100
                valorfinal=valor_categoria-descuento
            if  (pastor==3):
                descuento=(valor_categoria*23)/100
                valorfinal=valor_categoria-descuento
            if (pastor==4):
                descuento=(valor_categoria*4)/100
                valorfinal=valor_categoria-descuento
            print(f"Usted ah seleccionado El servicio Statsr y la categoria Basico, Debe pagar {valorfinal}")
    else:
        print("Usted ha ingresado un servicio invalido")
else:
    print("Ingrese una opcion valida")