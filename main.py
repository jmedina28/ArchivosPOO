from gestiones import *


def eleccion():
    
    variable = int(input("\nPor favor, introduzca qué desea ejecutar: \n --> 1: Lista de Aprobados.\n --> 2: Lista de suspensos.\n --> 3: Lista general.\n --> 4: Tabla.\n"))
    if variable == 1:
        listaaprobados()
    elif variable == 2:
        listasuspensos()
    elif variable == 3:
        listageneral()
    elif variable == 4:
        tabla()
    else:
        print("Sólo son válidos los valores 1, 2, 3 y 4.\n")
        eleccion()
eleccion()