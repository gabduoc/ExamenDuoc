import csv
import random
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos = [500000,700000,1100000,800000,2100000,600000,750000,2500000,300000,660000]
matriz = []


def asignasueldo(trabajadores,sueldos,matriz):
    for i in range(len(trabajadores)):
        nombre = trabajadores[i]
        sueldo = sueldos[i]
        matriz.append([nombre,sueldo])
        print(f"Trabajador: {nombre} Sueldo: {sueldo}")

def calificasueldo(matriz):
    if matriz == []:
        print("ERROR: No hay sueldos definidos")
        return()
    print("Sueldos menores a $800.000:")
    print("Nombre\t\tSueldo")
    for i in matriz:
        if i[1] < 800000:
            print(i[0],"   ",i[1])
    print("="*25)
    print("Sueldos entre $800.000 y 2000000:")
    print("Nombre\t\tSueldo")
    for i in matriz:
        if i[1] > 800000 and i[1] < 2000000:
            print(i[0],"   ",i[1])
    print("="*25)
    print("Sueldos superiores a 2000000:")
    print("Nombre\t\tSueldo")
    for i in matriz:
        if i[1] > 2000000:
            print(i[0],"   ",i[1])
    print("="*25)

def stats(matriz):
    if matriz == []:
        print("ERROR: No hay sueldos definidos")
        return()
    p = 0
    n = 0
    print("Sueldo mas alto:")
    for i in range(len(matriz)):
        if n < matriz[i][1]:
            n = matriz[i][1]
            p = i
    print(f"Nombre {matriz[p][0]} Sueldo: ${matriz[p][1]}")

    print("Sueldo mas bajo:")
    for i in range(len(matriz)):
        if n > matriz[i][1]:
            n = matriz[i][1]
            p = i
    print(f"Nombre {matriz[p][0]} Sueldo: ${matriz[p][1]}")

    print("Sueldo promedio:")
    total = 0
    for i in range(len(matriz)):
        total += matriz[i][1]
    print(f"${total/10}")
        
def reporte(matriz):
    if matriz == []:
        print("ERROR: No hay sueldos definidos")
        return()
    for i in range(len(matriz)):
        descuentosalud = matriz[i][1] * 0.07
        AFP = matriz[i][1] * 0.12
        print(f"Trabajador: {matriz[i][0]}\tSueldo Base: {matriz[i][1]}\tDescuento Salud: {round(descuentosalud)}\tDescuento AFP: {round(AFP)}\tSueldo Liquido: {matriz[i][1]-(round(descuentosalud) + round(AFP))}")

def importar(matriz):
    if matriz == []:
        print("ERROR: No hay sueldos definidos")
        return()
    with open("Sueldos.csv","w",newline="") as csfile:
        csvwriter = csv.writer(csfile)
        csvwriter.writerow(["Nombre","Sueldo"])
        for i in range(len(matriz)):
            csvwriter.writerow(matriz[i])

while True:
    opcion = str(input("Ingrese una opcion:\n"
                       "1. Asignar sueldos aleatorios\n"
                       "2. Clasificar sueldos\n"
                       "3. Ver estadísticas.\n"
                       "4. Reporte de sueldos\n"
                       "5. Exportar a csv\n"
                       "6. Salir del programa\n>"))
    match opcion:
        case "1":
            asignasueldo(trabajadores,sueldos,matriz)
        case "2":
            calificasueldo(matriz)
        case "3":
            stats(matriz)
        case "4":
            reporte(matriz)
        case "5":
            importar(matriz)
        case "6":
            print("Saliendo del programa...\nPrograma creador por Gabriel Zepeda [21.285.363.-1]")
            break
        case _:
            print("ERROR: Entrada invalida")
