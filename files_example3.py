import shutil
import os
# shutil.copy('hello3.txt', '..\\spam.txt')

# shutil.copytree('.\\do-przeniesienia', '..\\przeniesiony-backup')

# shutil.move('.\\do-przeniesienia\\hello3323.txt', '.\\')

# shutil.move('hello3323.txt', 'hello-new-name.txt')

# os.unlink('hello-new-name.txt')
# os.rmdir('.\\do-przeniesienia')
# shutil.rmtree('.\\do-przeniesienia')

for folderName, subfolders, filenames in os.walk('c:\\dev'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))

    for subfolder in subfolders:
        if 'fish' in subfolder:
            # os.rmdir(subfolder) USUNIE FOLDERY Z NAZWA FISH
            print('rmdir on ' + subfolder)

    for file in filename:
        # if file.endswith('.rozszerzenie'): ZMIENI NAZWĘ PLIKÓW z .rozszerzenie na .backup
            shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))