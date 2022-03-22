p = 0
calificaciones = open("calificaciones.csv", "r")
prueba = calificaciones.readline()
for i in range(16):
    prueba = calificaciones.readline().split(";")
    print(prueba)