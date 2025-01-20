myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.')

print(list(myCat.keys()))
print(list(myCat.values()))
print(list(myCat.items()))

for k in myCat.keys():
    print(k)

for v in myCat.values():
    print(v)

for k, v in myCat.items():
    print(k, v)

print(myCat.get('color', 0))
print(myCat.get('gol', 0))

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('apples', 0)) + ' apples to the picnic.')
print('I am bringing ' + str(picnicItems.get('napkins', 0)) + ' napkins to the picnic.')

myCat.setdefault('name', 'Puszek')