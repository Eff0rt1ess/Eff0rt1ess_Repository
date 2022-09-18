import requests
from bs4 import BeautifulSoup


url = 'https://pythonru.com/biblioteki/parsing-na-python-s-beautiful-soup'
request = requests.get(url)
page_structure = BeautifulSoup(request.text, 'html.parser')
text_on_page = page_structure.find('div', class_='td-post-content')
blocks_text = text_on_page.find_all('p')
for number, texts in enumerate(blocks_text, start=1):
    print(f'{number}. {texts.text}')