import copy

spam = ['hello', 'hi', 'howdy', 'heyas']

print(spam.index('howdy'))

spam.append('moose')

print(spam)

spam.insert(2, 'chicken')
print(spam)

spam.remove('heyas')
print(spam)

liczby = [5,9,6,4,7,3,58,604, 21, 43, 12, 5]
print(liczby)
liczby.sort()
print(liczby)

animals = ['elephant', 'ants', 'dog', 'badgers', 'cat']
animals.sort()
print(animals)
animals.sort(reverse=True)
print(animals)

spam = 42
cheese = spam
spam = 1000
print(spam)
print(cheese)

spamL = [0, 1, 2, 3, 4, 5]
cheeseL = spamL
cheeseL[1] = 'hello'
print(cheeseL)
print(spamL)

def eggs(someParameter):
    someParameter.append('Helllo')

spam = [1, 2, 3]
eggs(spam)

print(spam)

spam3 = ['A', 'B', 'C', 'D']
cheese3 = copy.deepcopy(spam3)
cheese3[1] = 42
print(cheese3)
print(spam3)