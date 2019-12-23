import time
lines = open('SKYTEAM(pdf)_order_by_fnumber.txt').readlines()
firstSpisok=[]
aa= time.time()
ciklTime= time.time()

for line in lines:
    a =line.strip().split(';')
    firstSpisok.append(a)
    secondSpisok.append(a)
print(len(firstSpisok))
i=0
print(firstSpisok[10])
sredneeVremya=[]
v=1
cvv=-1
number=0
frequentItem=''
pamyat=''
srednee=int(0)
while i<len(firstSpisok):
    timePoleta=firstSpisok[i][7].split(':')
    fi=int(timePoleta[0])*3600+int(timePoleta[1])*60+int(timePoleta[2])
    
    if firstSpisok[i][5]==pamyat:
        srednee=(srednee+fi)/2
    elif i!=0:
        sredneeVremya.append([pamyat, srednee])
        
        srednee=fi
        pamyat=firstSpisok[i][5]
    i+=1
vibros=[]
pamyat=''
count=0
j=0
c=0
b=0
pam=''
g=0
k=0
max=0
while j<len(firstSpisok):
    timePoleta=firstSpisok[j][7].split(':')
    fj=int(timePoleta[0])*3600+int(timePoleta[1])*60+int(timePoleta[2])
    if c==10000+b:
        b=c
        print(c/10000)
    while g < len(sredneeVremya):
        if firstSpisok[j][5]==pam:
            if fj>sredneeVremya[g][1]*3 and len(firstSpisok[j][5])>3:
                #vibros.append(firstSpisok[j])
                count+=1
                max=fj
                k=timePoleta
                break
            else:
                break
        else:
            if count==1:
                vibros.append([max, pam])
                print(k)
            count=0
            g+=1
            pam=sredneeVremya[g][0]
            break
            

    j+=1
    c+=1
        
b= time.time()
m=time.time() - aa
file = open('OUTPUT_100_3_srednee.TXT', 'w')
file.write(str(sredneeVremya))
print(str(m/60))
file.close()
file = open('OUTPUT_100_3_vibros.TXT', 'w')
file.write(str(vibros))
file.close()


