import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0    .3 Safari/605.1.15'}




hibbet = 'https://www.hibbett.com/men/mens-shoes/?start=0&sz=24'
def numOfPages(url):
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, 'html.parser')
    nop = soup.find('div',class_='results-hits')
    num = ''
    for n in nop.text:
        if n.isnumeric():
            num = num + str(n)
    print(num)
    return int(int(num)/24)

numOfPages(hibbet)
def getShoeNames(nop):
    for n in range(nop):
        hibbet = 'https://www.hibbett.com/men/mens-shoes/?start={0}&sz=24'.format(n)
        result = requests.get(hibbet,headers=headers)

        soup = BeautifulSoup(result.text, 'html.parser')

        shoes = soup.find_all('a',class_='name-link')
        for s in shoes:
            print(s.text + s.attrs['href'])

getShoeNames(numOfPages(hibbet))

urls=['https://www.hibbett.com/nike-air-force-1-low-white-mens-basketball-shoes/1P145.html?dwvar_1P145_color=1000&cgid=men-shoes#start=1&sz=24','https://www.hibbett.com/nike-air-vapormax-evo-anthracite-tech-grey-white-midnight-navy-mens-shoe/1P141.html?dwvar_1P141_color=0262&cgid=men-shoes#start=1&sz=24']
def findSizes(url):

    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, 'html.parser')

    sizes = soup.find_all('li', class_='selectable size')
    nums = []
    for s in sizes:
        num = ''
        for c in s.text:
            if c.isnumeric() or c == '.':
                num = num + str(c)
        nums.append(num)
    return nums


'''
for url in urls:
    num = findSizes(url)
    print(num)
'''
