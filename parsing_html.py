import bs4, requests

def getTitle(url):
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('tr.clickable-row:nth-child(1) > td:nth-child(4)')
    return elems[0].text.strip()



first_title = getTitle('https://bip.powiatpultuski.pl/rejestr-zmian/index')
print('Ostatnia zmieniona strona: ' + first_title)    

