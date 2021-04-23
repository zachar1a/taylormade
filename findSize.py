import requests
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup 


url = "https://www.nike.com/t/air-force-1-07-mens-shoe-xDpsTk/CT2302-100"

result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')
allP = soup.find_all('script')


for script in allP:

    print(script.text)
    if 'window.INITIAL_REDUX_STATE' in script.text:
        print("found")
