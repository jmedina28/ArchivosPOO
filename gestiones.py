
def listadiccionarios(calificaciones):
    separador = ";"
    with open(calificaciones) as tabla:
        next(tabla)  
        alumnado = []
        for linea in tabla:
            linea = linea.rstrip("\n") 
            columna = linea.split(separador)
            Apellidos, Nombre = columna[0], columna[1]
            Asistencia = columna[2]
            Parcial1, Parcial2 = columna[3],columna[4]
            Ordinario1, Ordinario2 = columna[5], columna[6]
            Practicas, OrdinarioPracticas = columna[7], columna[8]
            alumnado.append({
                "Apellidos": Apellidos,
                "Nombre": Nombre,
                "Asistencia": Asistencia,
                "Parcial 1": Parcial1,
                "Parcial 2": Parcial2,
                "Ordinario 1": Ordinario1,
                "Ordinario 2": Ordinario2,
                "Prácticas": Practicas,
                "Ordinario Prácticas": OrdinarioPracticas,
            })
        return alumnado

lista = listadiccionarios("calificaciones.csv")
lista[0]["Nota final"] = 5
<<<<<<< HEAD
print(lista[0]["Nombre"])
=======
print(lista[0]["Nombre"])
>>>>>>> 865b8dbe7de81714a1fc7e106bca5326690d2fcd
