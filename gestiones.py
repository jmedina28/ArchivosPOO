#Primera parte:
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
            Parcial1, Parcial2 = columna[3], columna[4]
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
# Segunda parte:
for i in range(len(lista)):
    lista[i]["Nota final"] = (float(lista[i]["Parcial 1"])*0.3)+(
        float(lista[i]["Parcial 2"])*0.3)+(float(lista[i]["Ordinario Prácticas"])*0.4)

print(lista)
# Tercera parte:
Aprobados = []
Suspensos = []
for i in range(len(lista)):
    if lista[i]["Asistencia"] >= 75 and float(lista[i]["Nota final"])>=5 and float(lista[i]["Parcial 1"]) >= 4 and float(lista[i]["Parcial 2"]) >= 4:
        Aprobados.append(lista.pop(i))
    else:
        Suspensos.append(lista.pop(i))
