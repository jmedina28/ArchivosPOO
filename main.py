from gestiones import *


def eleccion():
    
    variable = int(input("\nPor favor, introduzca qué ejercicio desea realizar: \n --> 1: Lista de Aprobados.\n --> 3: Lista de suspensos.\n --> 4: Lista general.\n"))
    if variable == 1:
        listaaprobados()
    elif variable == 2:
        listasuspensos()
    elif variable == 3:
        
    else:
        print("Sólo son válidos los valores 1, 2 y 3.\n")
        eleccion()
eleccion()