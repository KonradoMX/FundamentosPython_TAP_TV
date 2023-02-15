def nuevoTema(tema):
    print("\n==========", tema, "==========\n")

#Esto es un comentario.
if __name__ == "__main__":
    nuevoTema("Operadores artiméticos")
    print("Operador de división entera (10 // 3): ", 10//3)
    print("Operador de potencias (5 ** 5): ", 5 ** 5)
    print("Operador de cambio de signo (-5): ", -5)

    nuevoTema("Operadores lógicos")
    print("Operador and (True and False): ", True and False)
    #Actividad: Mostrar las tablas de verdad de los operador lógicos.

    nuevoTema("Operadores de comparación")
    print("2==3 ", 2==3)
    #Actividad: Agregar los demás oepradores de comparación.

    nuevoTema("Variables")
    variable1 = 10
    _variable2 = 34.2
    Variable3 = "Pepe"
    dos_palabras = "Hola"
    dosPalabras = "Hello"

    print(variable1, _variable2, Variable3, dos_palabras, dosPalabras)

    a, b, c = 98, 3.1416, "Bienvenido"
    print(a, b, c)

    nuevoTema("Enteros")
    w = 105
    x = 2074074873847821
    y = -345
    z = 0b00110011 #Entero en binario.
    h = 0xffa #Entero en hexadecimal.

    print(w, type(w))
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(h, type(h))

    nuevoTema("Flotantes")
    x = 1297.5
    print(x, type(x))
    y = 0.052829
    print(y, type(y))

    nuevoTema("Número complejos")
    x = -46j
    y = 12 + 45j
    z = 2j

    print(x, type(x))
    print(y, type(y))
    print(z, type(z))

    nuevoTema("Listas")
    a = [10, 20.5, "Python list"]
    print(a)
    a = ["lista2", 45, 16.3j]
    print(a)
    print(a[2])
    a[1] = 34.6
    print(a)

    nuevoTema("Tuplas")
    t = (25, "tupla", 5.6)
    print(t)
    print(t[1])
    #t[0] = "Modificado" #Operación no permitida en tuplas.
    #print(t)

    nuevoTema("Conjuntos")
    c = {50, 20, 10, 4, 8, 50}
    print(c)

    nuevoTema("Diccionarios")
    d = {1:"Valor1", "2":45}
    print(d, type(d))
    print(d["2"])
    print(d[1])

    nuevoTema("Cadenas")
    cadena1 = "Cadena entre comillas dobles"
    print(cadena1)
    cadena2 = 'Cadena entre comillas sencillas'
    print(cadena2)
    cadena3 = '''Cadena de
        varias
    líneas'''
    print(cadena3)
    print('''Otra cadena
    de  varias  líneas
    y tabladores''')