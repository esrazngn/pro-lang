# -*- coding: cp1254 -*-
#!/usr/bin/env python
def basamak_degeri_topla(sayi):
    deger = 0
    while sayi :
        basamak = sayi % 10 #Say�n�n mod�l�n� al�p basamak degiskenine atad�k.
        sayi = sayi / 10
        deger += basamak #Basamak degerini,deger adl� de�i�kene atad�k.
    print "toplam = %s"% (deger)
        
