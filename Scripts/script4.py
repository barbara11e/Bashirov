from collections import Counter 
import statistics 
from statistics import mode 
import datetime

lines = open('C:/Python27/Scripts/Passenger_countries.txt').readlines()
jews = open('strange_jews2.TXT', 'w') 
List = []
for line in lines:
    a = line.strip('" \n').split(';')
    b = a[1].split(',')
    c = a[2].split(',')
    d = []
    d.append(a[0])
    d.append(b)
    d.append(c)
    List.append(d)

List.pop(0)  

# List = [[1256], ['21-12-2019', '20-12-2019', '19-12-2019']
jews_countries = ["Israel"]

def most_common(List): 
    return(mode(List)) 

def date_check(_dates): 
    wrong_dates = []  
    for i in _dates:
        year, month, day = (int(x) for x in i.split('-'))    
        ans = datetime.date(year, month, day)
        if (ans.weekday() == 5):
            wrong_dates.append(str(ans))
    return wrong_dates

def making_list(pers_id, _date):    
    list0 = []
    list0.append(pers_id)
    list0.append(_date)
    return list0    

for el in List:
    el.append(most_common(el[2]))

for el in List:    
    if (el[3] in jews_countries):             
            jews.write(str(making_list(el[0], date_check(el[1]))) + '\n') 
jews.close()     
