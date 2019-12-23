from collections import Counter 
import statistics 
from statistics import mode 

indus_food =  ["HNML", "JNML", "VJM", "VLML", "VOML", "RVML", "VGML", "VVML", "AVML", "JNML"]
muslim_food =  ["MOML", "VJM", "VLML", "VOML", "RVML", "VGML", "VVML", "AVML", "JNML"]
vegan_food =  ["VJM", "VLML", "VOML", "RVML", "VGML", "VVML", "AVML", "JNML"]
jews_food = ["KSML", "KSMLS", "VJM", "VLML", "VOML", "RVML", "VGML", "VVML", "AVML", "JNML"]

d = []

lines = open('C:/Users/Default/Passenger-Food.txt').readlines()
for line in lines:
    a = line.strip('" \n').split(';')
    b = a[1].split(',')
    c = []
    c.append(a[0])
    c.append(b)
    d.append(c)

d.pop(0)
indus = open('strange_indus.TXT', 'w') 
muslim = open('strange_muslim.TXT', 'w') 
vegan = open('strange_vegan.TXT', 'w')  
jews = open('strange_jews.TXT', 'w') 

count_indus, count_muslim, count_vegan, count_jews  = 0,  0, 0, 0
count_strange_indus, count_strange_muslim, count_strange_vegan, count_strange_jews  = 0, 0, 0, 0 

def check(lst, sub):
   for i in range(0, len(lst)):
       if lst[i:i+len(sub)] == sub:
           return True
   return False

for el in d:
    result=list(set(el[1]) & set(indus_food))
    result2=list(set(el[1]) - set(indus_food))
    if( (  len(result) >0 ) and ( len (result2)>0 ) ):
        indus.write(str(el)+'\n') 
        count_strange_indus += 1

for el in d:
    result=list(set(el[1]) & set(muslim_food))
    result2=list(set(el[1]) - set(muslim_food))
    if( (  len(result) >0 ) and ( len (result2)>0 ) ):
        muslim.write(str(el)+'\n') 
        count_strange_muslim += 1

for el in d:
    result=list(set(el[1]) & set(jews_food))
    result2=list(set(el[1]) - set(jews_food))
    if( (  len(result) >0 ) and ( len (result2)>0 ) ):
        jews.write(str(el)+'\n') 
        count_strange_jews += 1

for el in d:
    result=list(set(el[1]) & set(vegan_food))
    result2=list(set(el[1]) - set(vegan_food))
    if( (  len(result) >0 ) and ( len (result2)>0 ) ):
        vegan.write(str(el)+'\n')   
        count_strange_vegan += 1

for el in d:
    result=list(set(el[1]) & set(indus_food))
    if( len(result) >0 ):
        count_indus += 1

for el in d:
    result=list(set(el[1]) & set(muslim_food))
    if( len(result) >0 ):
        count_muslim += 1

for el in d:
    result=list(set(el[1]) & set(jews_food))
    if( len(result) >0 ):
        count_jews += 1

for el in d:
    result=list(set(el[1]) & set(vegan_food))
    if( len(result) >0 ):
        count_vegan += 1
    

print(count_indus, count_strange_indus, count_strange_indus/count_indus)
print(count_muslim, count_strange_muslim, count_strange_muslim/count_muslim)
print(count_jews, count_strange_jews, count_strange_jews/count_jews)
print(count_vegan, count_strange_vegan, count_strange_vegan/count_vegan)

indus.close() 
muslim.close() 
vegan.close() 
jews.close()


   
