# -*- coding: cp1254 -*-
#!/usr/bin/python
def kok_hesapla(a,b,c):
    delta=(b**2)-(4*a*c)
    if delta>=0:
        birinci_kok=(-b+(delta**0.5))/(2*a)
        ikinci_kok=(-b-(delta**0.5))/(2*a)
        print "Denklemin birinci k�k�:",birinci_kok,"\n","Denklemin ikinci k�k�:",ikinci_kok
    else:
        print"Denklemin ger�el k�k� bulunmamaktad�r."
