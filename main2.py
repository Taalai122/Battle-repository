import requests
from bs4 import BeautifulSoup as BS

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def get_links(html):
    full_link = 'https://www.house.kg'
    soup = BS(html, 'html.parser')
    container = soup.find('div', class_='category-block sell')
    posts = container.find_all('div', class_='category-block-content-item')
    links = []

    for post in posts:
        link = post.find('a', href=True)
        if link:
            link_url = full_link + link['href']
            links.append(link_url)

    return links[:5]

def get_data(html):
    soup = BS(html, 'html.parser')
    container = soup.find('div', class_='main-content')
    post = container.find('div', class_='details-header')

    title = post.find('h1').text.strip()
    location = post.find('div', class_='address').text.strip()
    price = post.find('div', class_='price-dollar').text.strip()

    data = {
        'title': title,
        'location': location,
        'price': price,
    }
    return data

def save_in_txt(data):
    with open('data.txt', 'a') as file:
        file.write(f"Title: {data['title']}\n")
        file.write(f"Location: {data['location']}\n")
        file.write(f"Price: {data['price']}\n")
        file.write('\n')

def main():
    URL = 'https://www.house.kg'
    html = get_html(URL)

    with open('house_data.txt','w') as file:
        file.write("")

    if html:
        links = get_links(html)
        print("Ссылки и данные:")
        for link in links:
            post_html = get_html(link)
            if post_html:
                post_data = get_data(post_html)
                print("Ссылка:", link)
                print("Данные:", post_data)
                save_in_txt(post_data)
                print()
            else:
                print("Ошибка при получении HTML для ссылки:", link)
    else:
        print('Ошибка при получении HTML для основной страницы')
        


if __name__ == '__main__':
    main()
