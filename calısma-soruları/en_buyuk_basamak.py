# -*- coding: cp1254 -*-
def en_buyuk_basamak(sayi):
    a = repr(sayi) #Say�y� karakter dizisine �eviriyoruz.
    b = 0          #Basamak de�eri en k���k s�f�r olabilece�inden,de�i�kene s�f�r de�erini at�yoruz.
   
    for i in a :  
        i = int(i) #a daki ��eyi integer'a �eviriyoruz.
        if i >= b : b = i #e�er i deki de�er b dekinden b�y�kse,de�eri b ye at�yoruz
        else : pass     #K���k de�ilse de es ge�iyoruz.
    return b
