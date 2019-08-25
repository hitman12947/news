import requests
from bs4 import BeautifulSoup

def getNews():
    req = requests.get('https://www.bbc.com/')
    soup = BeautifulSoup(req.text, 'html.parser')

    link_text =[item.get_text().strip() for item in soup.find_all('a',class_='media__link')]
    links =[item.get('href') for item in soup.find_all('a',class_='media__link')]
    data = [link_text,links]
    return data

def main():
    pass

if __name__ == '__main__':
    main()
