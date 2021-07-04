casa = "verde"
print("antes mi casa era ",casa)

def cambiarColor(color):
    global casa
    casa = color

cambiarColor("rosa")

print("ahora es de color ",casa)
