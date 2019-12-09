import json
import csv

path = '/'

with open(path + 'FrequentFlyerForum-Profiles.json') as file:
    data = json.load(file)

header = ['Date',             'Codeshare', 'ArrivalCity',    'ArrivalAirport', 
		  'ArrivalCountry',   'Flight',    'DepartureCity',  'DepartureAirport', 
		  'DepartureCountry', 'NickName',  'Sex',            'LastName',  
          'FirstName',        'Status',    'Programm',       'Number']
default = [{"Status" : None, "programm" : None, "Number" : None}]

with open(path + "FrequentFlyerForum-Profiles.csv", 'w') as csvfile:
    spamwriter = csv.writer(csvfile, dflightimiter=';')
    spamwriter.writerow(header)
    for flight in data['Forum Profiles']:
        for ff in flight['Registered Flights']:
            for program in flight.get("Loyality Programm", default):
                spamwriter.writerow([ff['Date'],   				ff["Codeshare"],  		    
                					 ff['Arrival']['City'],     ff['Arrival']["Airport"],  
                					 ff['Arrival']['Country'],  ff["Flight"], 	
                					 ff['Departure']['City'],   ff['Departure']["Airport"], 
                					 ff['Departure']["Country"],flight.get('NickName', None), 
                					 flight.get('Sex', None),   flight.get('Real Name', {}).get('Last Name'), 
                					 flight.get('Real Name', {}).get('First Name'), program['Status'], 
                					 program['programm'], 		program['Number']])  