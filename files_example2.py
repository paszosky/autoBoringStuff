helloFile = open('c:\\dev\\Hello.txt')

content = helloFile.read()
helloFile.close()
print(content)

# helloFile.readlines()

helloFile = open('hello3.txt', 'a')
helloFile.write('Hello!!!! Piszemy tutaj po raz drugi \n Dodajemy kolejną linię')
helloFile.close()