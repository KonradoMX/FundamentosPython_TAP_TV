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

    print("hola")