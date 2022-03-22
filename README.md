<h1 align="center">Archivos</h1>

<h3 align="center">Autor de este proyecto:</h3>

1. [@jmedina28](https://github.com/jmedina28)
---
En este [repositorio](https://github.com/jmedina28/ArchivosPOO) quedan resuelto el ejercicio de archivos para POO. Para llevar a cabo el proyecto me he documentado a través de la teoría que se encuentra en el campus virtual y de diversas fuentes que he encontrado.
***
## Ejercicio Archivos

En este ejercicio he pasado de tener un archivo .csv a tener una lista de diccionarios, la cual posteriormente he dividido en un listad general, uno de aprobados y otro de suspensos. Para realizar este ejercicio me he documentado especialmente de cara a convertir el .csv en una lista de diccionarios.

El código empleado para resolverlo es el siguiente: 

```python
# Primera parte:
def listadiccionarios(calificaciones):
    separador = ";"
    with open(calificaciones, encoding="UTF8") as tabla:
        next(tabla)
        alumnado = []
        for linea in tabla:
            linea = linea.rstrip("\n")
            columna = linea.split(separador)
            Apellidos, Nombre = columna[0], columna[1]
            Asistencia = columna[2]
            Parcial1, Parcial2 = columna[3], columna[4]
            Ordinario1, Ordinario2 = columna[5], columna[6]
            Practicas, OrdinarioPracticas = columna[7], columna[8]
            alumnado.append({
                "Apellidos": Apellidos, "Nombre": Nombre,
                "Asistencia": Asistencia,
                "Parcial 1": Parcial1, "Parcial 2": Parcial2,
                "Ordinario 1": Ordinario1, "Ordinario 2": Ordinario2,
                "Prácticas": Practicas, "Ordinario Prácticas": OrdinarioPracticas,
            })
        return alumnado


lista = listadiccionarios("calificaciones.csv")
# Segunda parte:
for i in range(len(lista)):
    lista[i]["Nota final"] = (float(lista[i]["Parcial 1"])*0.3)+(
        float(lista[i]["Parcial 2"])*0.3)+(float(lista[i]["Ordinario Prácticas"])*0.4)

# Tercera parte:
Aprobados, Suspensos = [], []

for i in range(len(lista)):
    if float(lista[i]["Asistencia"]) >= 75 and float(lista[i]["Nota final"]) >= 5 and float(lista[i]["Parcial 1"]) >= 4 and float(lista[i]["Parcial 2"]) >= 4:
        Aprobados.append(lista[i])
    else:
        Suspensos.append(lista[i])

Suspensos, Aprobados = sorted(Suspensos, key=lambda k: k["Apellidos"]), sorted(
    Aprobados, key=lambda k: k["Apellidos"])


def listasuspensos():
    print("\nLa lista de suspensos ordenada alfabéticamente por apellidos es la siguiente:\n ")
    for i in range(len(Suspensos)):
        if Suspensos[i]["Nota final"] >= 5:
            print(Suspensos[i]["Nombre"], Suspensos[i]
                  ["Apellidos"] + " con una nota final de: 4")
        else:
            print(Suspensos[i]["Nombre"], Suspensos[i]["Apellidos"] +
                  " con una nota final de: " + str(Suspensos[i]["Nota final"]))
    print("\n" + str(Suspensos))


def listaaprobados():
    print("\n\nLa lista de aprobados ordenada alfabéticamente por apellidos es la siguiente: \n")
    for i in range(len(Aprobados)):
        print(Aprobados[i]["Nombre"], Aprobados[i]["Apellidos"] +
              " con una nota final de: " + str(Aprobados[i]["Nota final"]))
    print("\n" + str(Aprobados))


def listageneral():
    print("\nLa lista general ordenada alfabéticamente por apellidos es la siguiente:\n ")
    General = Aprobados + Suspensos
    General = sorted(General, key=lambda k: k["Nombre"])
    for i in range(len(General)):
        if float(General[i]["Asistencia"]) >= 75 and float(General[i]["Nota final"]) >= 5 and float(General[i]["Parcial 1"]) >= 4 and float(General[i]["Parcial 2"]) >= 4:
            print(General[i]["Nombre"], General[i]["Apellidos"] +
                " con una nota final de: " + str(General[i]["Nota final"]) + " APROBADO")
        else:
            print(General[i]["Nombre"], General[i]["Apellidos"] +
                " con una nota final de: " + str(General[i]["Nota final"]) + " SUSPENSO")
    print("\n" + str(General))
```
