#-*- coding: utf-8 -*-
#sencillo algoritmo para calcular una n cantidad de notas para un promedio
while True:
    n=float(raw_input("ingrese la nota a calcular: "))
    i = 0
    acum = 0
    if i >= 0 and acum >= 0:
        i = i + 1
        acum = acum + n
    cal_prom = raw_input("¿desea calcular el promedio? s/n ")
    if cal_prom == "s":
        prom = acum / i
        break
print "el promedio del alumno es :", prom
