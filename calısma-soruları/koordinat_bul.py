# -*- coding: cp1254 -*-
#!/usr/bin/python

def koordinat_bul(x,y):
    if x>0 & y>0:
        print"1.b�lge"
    elif x<0:
        if y>0:
            print"2.b�lge"
        else:
            print"3.b�lge"
    elif x<0 & y<0:
        print"4.b�lge"
