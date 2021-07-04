def esPalindromo(texto): return True if texto[::-1].replace(" ", "") == texto.replace(" ", "") else False

texto = input("Ingrese una palabra o frase para saber si califica como palindromo: ")
palindromo = esPalindromo(texto)
resultado = f"{texto} califica como palindromo y su largo es {len(texto)}" if palindromo else f"No es palindromo y su largo es: {len(texto)}"
print(resultado)


def funcion():
    maximo = int(input("Ingrese un número entero del 10 al 15 para obtener el número maximo en la serie de Fibonacci: "))
    if(maximo < 10 or maximo > 15):
        return(False)
    else: 
        a = 0
        b = 1
        for k in range(maximo):
            c = a+b
            a = b
            b = c
        return b

numMax = funcion()
valido = ""

if (numMax):
    print(numMax)
else:
    print("Ingresaste un número invalido")