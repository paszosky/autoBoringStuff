def hello(name):
    print('hello ' + name)

hello('Alice')
hello('Bob')

def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)

print('cat', 'dog', 'mouse')
print('cat', 'dog', 'mouse', sep='ABC')

# scopes


def spam():
    global eggs
    eggs = 'hello'
    print(eggs)
spam()
eggs = 42


print(eggs)