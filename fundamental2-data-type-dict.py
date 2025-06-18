"""
The dictionary data type simply connect KEY and VALUE
KVP = Key Value Pair
"""

dict_id_eng = {'anak':'son', 'ibu':'mother', 'ayah':'father','suami':'husband', 'istri':'wife'}

print(dict_id_eng)
print(dict_id_eng['ayah'])
print(dict_id_eng['suami'])
print(dict_id_eng['ibu'])
print(dict_id_eng['istri'])

print('\nThis data sending from server website, for give a information about driver at around using apps')
data_from_website = {
    'date': 'June, 18 2025',
    'driver_list': [
        {'Name':'Ali', 'distance': 20},
        {'Name':"Aji", 'distance': 50},
        {'Name':'Yura', 'distance': 100},
        {'Name':'Yuyu', 'distance': 1000},
    ]
}
print(data_from_website)
print(f"\nAround driver {data_from_website['driver_list']}")
print(f"Driver #1 {data_from_website['driver_list'][0]}")
print(f"Driver #4 {data_from_website['driver_list'][3]}")
print(f"The nearest driver is distance away {data_from_website['driver_list'][0]['distance']} meter")
