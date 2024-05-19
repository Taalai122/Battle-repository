import requests
from bs4 import BeautifulSoup as BS

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def get_data(html):
    soup = BS(html,'html.parser')
    container = soup.find('div', class_='browsing-card-group browsing-card-group--text-top-aligned')
    products = container.find_all('div',class_='meka-browsing-card')







def main():
    URL = 'https://us.shop.battle.net/en-us'
    html = get_html(URL)