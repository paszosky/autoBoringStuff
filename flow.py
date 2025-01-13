name = 'Alice'
if name == 'Alice':
    print('Hi Alice')
print('Done')


basket = 'pie'
if basket == 'apple':
    print('Apple in basket')
else:
    print('No apple in basket')


name = 'Bob'
age = 130
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('you are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')

print('Enter a name')
name = input()
if name:
    print('Thank you for entering a name.')
else:
    print('You did not enter a name')
    