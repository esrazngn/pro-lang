# -*- coding: cp1254 -*-
import math
def mutlak_genel():
    while True:
        s = input("Karma��k say�lar i�in 1,tamsay�lar i�in 2,ondal�k say�lar i�in 3,��kmak i�in 4 giriniz:")
        if s==1 :    
            a = input("Ger�el k�sm� giriniz:")
            b = input("sanal k�sm� giriniz:")
            w = math.sqrt((a**2)+(b**2))
            print "Tamsay�n�n mutlak de�eri:",w
        elif s==2 :
            a = input("Tamsay�y� giriniz:")
            if a<0 :
                t = -1*a
                print "Tamsay�n�n mutlak de�eri:",t
            else :
                print "Tamsay�n�n mutlak de�eri:",a
        elif s==3 :
            a = input("Ondal�kl� say�y� giriniz:")
            if a<0 :
                k = -1*a
                print "Ondal�kl� say�n�n mutlak de�eri:",k
            else :
                print "Ondal�kl� say�n�n de�eri:",a
        else :
            break
