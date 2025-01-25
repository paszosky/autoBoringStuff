import os

print(os.path.join('folder1', 'folder2', 'folder3', 'file.png'))

print(os.getcwd())

print(os.path.abspath('README.md'))

print(os.path.getsize('README.md'))

print(os.listdir('.\\'))

totalSize = 0
for filename in os.listdir('.\\'):
    if os.path.isfile(os.path.join('c:\\dev\\python\\autoBoringStuff', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('c:\\dev\\python\\autoBoringStuff', filename))

print(totalSize)

