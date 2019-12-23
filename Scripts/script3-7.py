import time
import copy
lines = open('3_7script.txt', encoding='UTF-8').readlines()
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
i=0
print(i)
spisOkonch1=[]
spisOkonch2=[]
v=1
cvv=0
frequent=0
maxFrequent=0
number=0
frequentItem=''
pamyatI=['' for x in range(8)]
pamyatJ=[]
while i<len(firstSpisok):
    k=0
    t=0
    count=-1
    j=i
    if cvv*len(firstSpisok)>(int(len(firstSpisok)*len(firstSpisok))*v*0.01):
            print('Ready .......'+str(v)+'%')
            print(time.time()-ciklTime)
            ciklTime= time.time()
            v+=1
    frequent=0
    pamyatI.clear()
    pamyatI=copy.copy(firstSpisok[i])
    if firstSpisok[i][3]!=firstSpisok[i-1][3] or firstSpisok[i][5]!=firstSpisok[i-1][5] and i>0:
        while j< len(firstSpisok):
                count+=1
                dataI=firstSpisok[i][4].split('.')
                dataJ=firstSpisok[j][4].split('.')
                fi=int(dataI[0])
                fj=int(dataJ[0])
                mi=int(dataI[1])
                mj=int(dataJ[1])
                if mi==mj and fi==fj-1:
                    break
                if (mi<mj and ((fi==30 and fj==1) or (fi==31 and fi==1) or (fi==28 and fi==1) or (fi==29 and fi==1)))\
                or mi<mj-1:
                    break

                if firstSpisok[i][3]==firstSpisok[j][3] and dataI[2]==dataJ[2] and\
                firstSpisok[i][6]!=firstSpisok[j][6] and firstSpisok[i][7]!=firstSpisok[j][6]:
                    if ( fi==fj or ((fi==30 and fj==30) or (fi==31 and fi==31) or (fi==28 and fi==28) or (fi==29 and fi==29))):\
                    #and (firstSpisok[i][16]!=firstSpisok[j][16]):
                        spisOkonch1.append(firstSpisok[i])
                        spisOkonch2.append(firstSpisok[j])
                        #print(firstSpisok[i])
                        frequent+=1
                        if frequent>maxFrequent:
                            maxFrequent=frequent
                            frequentItem=str(firstSpisok[i])
                j+=1
        
    i+=1
    cvv+=1
    
    
print(frequentItem)
b= time.time()
m=time.time() - aa
file = open('OUTPUT17_izraznihGorodovMenee2Dney1.TXT', 'w')
file.write(str(spisOkonch1))
print(str(m/60))
file.close()

file = open('OUTPUT17_izraznihGorodovMenee2DneyVtoraya1.TXT', 'w')
file.write(str(spisOkonch2))
print(str(m/60))
file.close()

