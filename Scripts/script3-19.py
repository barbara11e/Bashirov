import time
import copy
lines = open('3_7_1.txt', encoding='UTF-8').readlines()
firstSpisok=[]
secondSpisok=[]
aa= time.time()
ciklTime= time.time()
for line in lines:
    a =line.strip().split(';')
    firstSpisok.append(a)
    secondSpisok.append(a)
out=[]
hernya=[]

spisOkonch1=[]
spisOkonch2=[]
v=1
cvv=0
frequent=0
maxFrequent=0
number=0
count=0
frequentItem=''
pamyatI=[]
pamyatI = copy.copy(firstSpisok[100000])
pamyatJ=[]
t=0
i=0
print(firstSpisok[0])
while i<len(firstSpisok):
    k=0
    
    j=i
    if cvv==10000:
        cvv=0
        t+=1
        print(t)
    uy=firstSpisok[i][4].split('.')
    if int(uy[1])>1 and int(uy[1])<12:
        if firstSpisok[i][3]==pamyatI[3]:
            count=count+1
        else:
            if count==1 :
                spisOkonch1.append(firstSpisok[i-1])
                print(firstSpisok[i-1])
                print(count)
            pamyatI.clear()
            pamyatI = copy.copy(firstSpisok[i])
            count=1
  
    i+=1
    cvv+=1
    
print(frequentItem)
b= time.time()
m=time.time() - aa
file = open('OUTPUT18_letayut1razvgod.TXT', 'w')
file.write(str(spisOkonch1))
print(str(m/60))
file.close()

file = open('OUTPUT18_letayut1razvgodVtoraya.TXT', 'w')
file.write(str(spisOkonch2))
print(str(m/60))
file.close()
