import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'  # address
response = requests.get(url)  # make get-request </>
soup = BeautifulSoup(response.text, 'html.parser')  # return html structure </>
all_dresses_blocks = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

for number, information in enumerate(all_dresses_blocks, start=1):
    NameDress = information.find('h4', class_='card-title').text.replace('\n', '')
    PriceDress = information.find('h5').text
    print(f'{number}.  {NameDress} — {PriceDress}')

pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')

for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        hrefval = link.get('href')
        urls.append(hrefval)

n = 10
for slug in urls:
    newUrl = url.replace('?page=1', slug)
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for n, i in enumerate(items, start=n):
        itemName = i.find('h4', class_='card-title').text.strip()
        itemPrice = i.find('h5').text
        print(f'{n}.  {itemPrice} — {itemName}')
