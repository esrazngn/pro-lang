# -*- coding: cp1254 -*-
#!/usr/bin/python
import math
def kok_hesapLa(a,b,c):
    birinci_kok=(-b+(math.sqrt((b**2)-(4*a*c))))/(2*a)
    ikinci_kok=(-b-(math.sqrt((b**2)-(4*a*c))))/(2*a)
    print "Denklemin birinci k�k�:",birinci_kok,"\nDenklemin ikinci k�k�:",ikinci_kok
