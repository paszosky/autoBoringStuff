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