import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '870', 'Valencia', 'St.']

# check if command line arguments were passed
if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.'] Kolska 12, 01 045 Warszawa
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.pl/maps/place/<ADDRESS>
webbrowser.open('https://www.google.pl/maps/place/' + address)