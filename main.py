import requests
from bs4 import BeautifulSoup as BS

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def get_links(html):
    soup = BS(html,'html.parser')
    container = soup.find('div', class_='container-fluid my-3x md:my-4x')
    posts = container.find_all('a', class_='p-2x flex flex-col gap-y-2x')

    links = []
    for post in posts:
        link = post.get('href')
        full_link = 'https://us.shop.battle.net/en-us'+ link
        links.append(full_link)
    return links 

def get_data(html):
    soup = BS(html,'html.parser')
    container = soup.find('div', class_='app-container')
    posts = container.find_all('li',class_='ng-star-inserted')
    title = posts.find('dt', class_='meka-browsing-card__details__heading').text.strip()
    genre = posts.find('dd', class_='meka-browsing-card__details__highlight').text.strip()
    price = posts.find('div',class_='price ng-star-inserted')

    data  = {
        'title' :title,
        'genre' :genre,
        'price':price,
        
    }
    return data

def main():
    URL = 'https://us.shop.battle.net/en-us'
    html = get_html(URL)
    

if __name__ == '__main__':
    main()