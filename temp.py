#-*- coding: utf-8 -*-
"""script para calcular la temperatura en grados celcius y farengeiht """
while resp == 'S' or resp == 's':
        temp=float(raw_input("ingrese su temperatura: "))

        opti=str(raw_input("¿desea convertir a (C)elcius o a (F)arengeith?: "))

        if opti == 'C' or opti == 'c':
            conv = ((temp-32) * 5)/9
            print "su temperatura en celsius es: ", conv
        else:
            if opti == 'F' or opti == 'f':
                conv = (temp * 9)/5 + 32
                print "su temperatura en Farengeith es:", conv
        resp=str(raw_input("¿desea ingresar otra temperatura? (S/N): "))

        if resp == 'N' or resp =='n':
            break
