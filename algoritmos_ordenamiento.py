# Brandon Alain Cruz Ruiz   198573
# Análisis de algoritmos
# Mini proyecto: Merge Sort VS Insertion Sort

from datetime import datetime
from random import randint


def Merge_Sort(a):
    # Si la longitud de la lista es menor o igual a 1
    # el arreglo está ordenado # Caso base
    if len(a) <= 1:
        return a
    mid = int(len(a) / 2)
    # Llamada recursiva con a[0,..., len(a)/2]
    left = Merge_Sort(a[:mid])
    # Llamada recursiva con a[len(a)/2 + 1, len(a)]
    right = Merge_Sort(a[mid:])
    res = []
    # Iteramos hasta vaciar alguno de los dos arreglos
    while len(left) > 0 and len(right) > 0:
        l_0 = left[0]
        r_0 = right[0]
        # Si el primer elemento de la derecha es menor
        # agregamos el elemento de la derecha al resultado
        if l_0 > r_0:
            res.append(r_0)
            # Quitamos el elemento
            right.pop(0)
        # En otro caso, agregamos el elemento de la izquierda
        else:
            res.append(l_0)
            # Quitamos el elemento
            left.pop(0)

    # Iteramos sobre los elementos sobrantes del arreglo left y right
    for value in left:
        res.append(value)
    for value in right:
        res.append(value)

    return res


def Insertion_Sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    return a


def Generate_Array(len_array):
    a = []
    for _ in range(len_array):
        a.append(randint(0, 10000))
    return a


def Prueba_Individual():
    print("Longitud del arreglo:")
    num = int(input())
    a = Generate_Array(num)
    time_insertion_start = datetime.now()
    res_insertion = Insertion_Sort(a)
    time_insertion_end = datetime.now() - time_insertion_start
    time_merge_start = datetime.now()
    res_merge = Merge_Sort(a)
    time_merge_end = datetime.now() - time_merge_start
    print(
        f"Insertion Sort: \n Tiempo: {time_insertion_end.microseconds/1000} s \n Arreglo ordenado: {res_insertion}"
    )
    print(f"********")
    print(
        f"Merge Sort: \n Tiempo: {time_merge_end.microseconds/1000} s \n Arreglo ordenado: {res_merge}"
    )


def Run_Test(len_array):
    a = Generate_Array(len_array)
    time_insertion_start = datetime.now()
    Insertion_Sort(a)
    time_insertion_end = datetime.now() - time_insertion_start
    time_merge_start = datetime.now()
    Merge_Sort(a)
    time_merge_end = datetime.now() - time_merge_start
    return time_insertion_end, time_merge_end


def Tiempo_Promedio():
    print("¿Cuántas veces se debe ejecutar el ordenamiento?")
    n = int(input())
    print("Entradas mínimas del arreglo:")
    n_min = int(input())
    print("Entradas máximas del arreglo:")
    n_max = int(input())
    num = randint(n_min, n_max)
    print(f"Se correra {n} veces el experimento con longitud del arreglo {num}")
    sum_insertion = sum_merge = 0
    for i in range(n):
        insertion, merge = Run_Test(num)
        sum_insertion += insertion.microseconds / 1000
        sum_merge += merge.microseconds / 1000
    print(f"Promedio de tiempo para Insertion Sort: {sum_insertion/n} segundos")
    print(f"Promedio de tiempo para Merge Sort: {sum_merge/n} segundos")


def Main():
    option = 0
    while option != 1 and option != 2:
        print("¿Qué deseas ejecutar?")
        print("1 - Pruebas individuales")
        print("2 - Promedio en n pruebas")
        option = int(input())
        if option == 2:
            Tiempo_Promedio()
        elif option == 1:
            Prueba_Individual()


Main()
