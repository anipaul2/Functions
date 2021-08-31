import pprint
Person3 = { 'Name' : 'Ford Prefect',
            'Gender' : 'Male',
            'Occupation' : 'Researcher',
            'Home Planet' : 'Betelgeuse Seven'}
#print(Person3)
#print(Person3['Home Planet'])
#print(Person3['Name'])
#print(Person3)
#Person3['Age'] = 33
#print(Person3)
people = {}
people['ford'] = { 'Name' : 'Ford Prefect',
                   'Gender' : 'Male',
                   'Occupation' : 'Researcher',
                   'Home Planet' : 'Betelgeuse Seven'}
people['Arthur'] = { 'Name' : 'Arthur Dent',
                     'Gender' : 'Male',
                     'Occupation' : 'Sandwich-Maker',
                     'Home Planet' : 'Earth'}
people['Trillian'] = {'Name' : 'Tricia McMillan',
                      'Gender' : 'Female',
                      'Occupation' : 'Mathematician',
                      'Home Planet' : 'Earth'}                     
people['Robot'] = {'Name' : 'Marvin',
                   'Gender' : 'Unknown',
                   'Occupation' : 'Paranoid Android',
                   'Home Planet' : 'Unknown'} 
#pprint.pprint(people)                           
print(people['Arthur'] ['Name'])