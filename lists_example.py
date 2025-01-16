spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0])

print(spam)
spam[1] = 'Hello'
print(spam)

hej = list("Nowa lista")
print(hej)

for i in range(4):
    print(i)

print(list(range(4)))

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

cat = ['fat', 'orange', 'loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]

size, color, disposition = cat # to przypisuje poszczegolne elementy listy do zmiennych

print(color)

a, b, c = 'aaa', 'bbb', 'ccc'
print(a)