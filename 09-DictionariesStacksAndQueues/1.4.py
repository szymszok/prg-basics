person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

print(person['name'])
print(person['hobby'])
person['surname'] = 'Nowak'
person['married'] = False
person['gender'] = 'Male'
person['hobby'].append('bicycle')
person['phone']['work'] = '313131444'

for item, items in person.items():
    print(f'{item}: {items}')


