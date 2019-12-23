#10

lines3 = open('data-1575930302703.csv').readlines()
spisok1=[]
spisok2=[]
spisokVibrosov=[]
print(spisokVibrosov)
for line in lines3:
    a =line.strip().split(',')
    number = a[0]
    surname=a[1]
    first_name = a[2]
    middle_name=a[3]
    spisok1.append(a)
    spisok2.append(a)

for i in spisok1:
    k=0
    for j in spisok2:
        if i[0]==j[0] and i[0]!='NULL':
            k+=1
    if k>1:
        spisokVibrosov.append(i)





file = open('OUTPUT.TXT', 'w')
file.write(str(spisokVibrosov))
file.close()
