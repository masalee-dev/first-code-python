print('switch data type => simple data type')
children1 = "Komar"
children2 = "Martinah"
children3 = "Ratna Dewi"
children4 = "Haeder Ali"
children5 = "Aji Nur Febrian"

print(children1)
print(children2)
print(children3)
print(children4)
print(children5)

print('\nList data type/list/array')
children = ['Komar', 'Martinah', 'Ratna Dewi','Haeder Ali','Aji Nur Febrian']
print(children)
children.append('Yura')
print(children)

print('\nSay Hi to children number-2')
print(f'Hi {children[1]}!')

print('\nSay Hi All')
for a in children:
    print(f'Hi {a}!')

#another way
print('\nSay Hi All')
for a in range(0, len(children)):
    print(f'{a+1}. Hai {children[a]}')
