import requests
from bs4 import BeautifulSoup as BS

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def get_data(html):
    soup = BS(html,'html.parser')
    container = soup.find('div', class_='app-container')
    posts = container.find_all('li',class_='ng-star-inserted')
    print(posts)


    data = []
    for i in posts:
        title = i.find('dt', class_='meka-browsing-card__details__heading').text.strip()
        genre = i.find('dd', class_='meka-browsing-card__details__highlight').text.strip()
        price = i.find('div',class_='price ng-star-inserted')
        
        data.append([title, genre, price])
    return data[:10]


def main():
    URL = 'https://us.shop.battle.net/en-us'
    html = get_html(URL)
    

if __name__ == '__main__':
    main()