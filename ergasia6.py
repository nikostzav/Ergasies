from random import *
platos=int(input("Mhkos: "))
mhkos=int(input("Platos:"))
Bombs=int(input("Bombs: "))
if Bombs<=platos*mhkos:
    m=[[0 for x in range(platos)] for y in range(mhkos)]
    while Bombs>0:
            x=randint(0,mhkos-1)
            y=randint(0,platos-1)
            if m[x][y]==0:
                Bombs-=1
            m[x][y]=1
    for i in m:
        print(*i,sep=" ")
else :
    print ("Perissoteres bobmbes apo koutakia")
