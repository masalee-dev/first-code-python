user = {
    'id':1,
    'name':'Haeder Ali',
    'username':'masalee',
    'email':'haederalee@gmail.com',
    'address': {
        'street': 'Bogasari',
        'suite': 'No 17',
        'city': 'Bogor',
        'zipcode': '16980',
    }
}

print(user['address']['zipcode'])

print('\nChange dict to JSON')
import json
result = json.dumps(user)
print(result)

with open('result.json', 'w') as file:
    json.dump(user, file)