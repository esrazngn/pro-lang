def dogrula(tc):
    liste = []
    s_tc = str(tc)
    if len(s_tc) == 11 and tc > 0 and type(tc) == long :
        for i in range(len(s_tc)):
            liste.append(tc%10)
            tc = tc /10
        liste.reverse()
        sart1,sart2 = 0,0
        for i in range(len(liste)-2):
            if i % 2 == 0:
                sart1 += 7*liste[i]
            else : sart2 += liste[i]
        sart�m1 = (sart1-sart2)%10
        toplam = 0
        for i in range(len(liste)-1):
            toplam += liste[i]
        sart�m2 = toplam%10
        if sart�m1 == liste[-2] and sart�m2 == liste[-1]:
            print "TC kimlik numaras� ge�erlidir."
        else :print "TC kimlik numaras� ge�erli de�ildir."
    else : print "L�tfen 11 basamakl� bir tamsayi giriniz!"
