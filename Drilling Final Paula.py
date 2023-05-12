nombreslistado = ("Harry Houdini , Newton, David Blaine , Hawking , Messi , Teller , Einstein , Pele , Juanes")
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]


def hacer_grandioso():
    for i in range(len(magos)):
        magos[i] = "El Gran " + magos[i]

def imprimir_nombres():
    print("==>Los Magos:")
    for nombre in magos:
        print(nombre)
    print("==> Los Científicos:")
    for nombre in cientificos:
        print(nombre)

    
otros = []  
otros.append("Messi") 
otros.append("Pele")  
otros.append("Juanes") 

print ("Todos los integrantes de la lista:", nombreslistado)
print ()
hacer_grandioso()

imprimir_nombres()
print("==> Otros son: ", otros)
print ()
print ("FIN")


