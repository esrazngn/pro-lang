#!/usr/bin/env python
while True:
    try:
        print "Girilen en b�y�k say�:",reduce(lambda x,y:max(x,y),input("L�tfen say�lar� aralar�na virg�l koyarak giriniz:"))
        break
     except TypeError : return "HATA!"  
                                              


       
