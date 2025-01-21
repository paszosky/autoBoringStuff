sampple = "That is Alice's cat."
samp2 = 'Say hi to Bob\' mother.'
print('Hello there \n How are you?\n\t I\'m fine')

print(r'That is Carol\'s cat.') # row string

# multi line strin """
print("""Dear Alice,
      Eve's cat has been arrested for catnapping, cat burglary,
      and extortion.
      Sincerely,
      Bob.""")

spam = 'Hello world!'

print(spam[0])

print(spam.upper())

print(spam[2].startswith('l'))

dziel = 'My name is simon'.split()
print(dziel)
dziel2 = 'My name is simon'.split('m')
print(dziel2)

print('hello'.ljust(20))
print('bye'.rjust(20, '*'))
print('welcom'.center(20, '='))

print('     x     '.strip())
print('     x     '.rstrip())
print('     x     '.lstrip())

print('Hello there'.replace('e', 'XYZ'))