book = ['Bungkam Suara', 'Aku Bukan Sarjana Kertas', 'Angsa dan Kelelawar', "Alegori 420"]
print(book) # Variable book view

for t in book:
    print(t) # For in Process

# View book contents at a specific index
print(book[0])
print(book[2])

for i in range(0, len(book)):
    print(book[i]) # For in with range

print('\nCLear List')
book.clear() # delete command in List
for i in range(0, len(book)):
    print(book[i])

book = ['Bungkam Suara', 'Aku Bukan Sarjana Kertas', 'Angsa dan Kelelawar', "Alegori 420"]
book[0] = 'Seni Berbicara' # change command in List
print('Change tittle first book')
for i in range (0, len(book)):
    print(book[i])

print('\nTake second book')
take = book.pop(1) # taken command in List
for i in range (0, len(book)):
    print(book[i])

print('\nTittle taken of the book')
print(take)

print('\nCommand del')
book = ['Bungkam Suara', 'Aku Bukan Sarjana Kertas', 'Angsa dan Kelelawar', "Alegori 420"]
del book[0]
for i in range(0, len(book)):
    print(book[i])

print('\nCommand del with list comprehension')
book = ['Bungkam Suara', 'Aku Bukan Sarjana Kertas', 'Angsa dan Kelelawar', "Alegori 420"]
del book[:] # Command list comprehension
for i in range(0, len(book)):
    print(book[i])

book = ['Bungkam Suara', 'Aku Bukan Sarjana Kertas', 'Angsa dan Kelelawar', "Alegori 420"]
del book[0::2] # START:END:START
for i in range(0, len(book)):
    print(book[i])