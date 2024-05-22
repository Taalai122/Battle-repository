import requests
from bs4 import BeautifulSoup as BS

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def get_links(html):
    full_link = 'https://us.shop.battle.net/en-us'
    soup = BS(html, 'html.parser')
    container = soup.find('ul', class_='browsing-card-group-layout browsing-card-group-layout--auto browsing-card-group-layout--auto--full-width browsing-card-group-layout--quantity-responsive')
    posts = container.find_all('div', class_='browsing-card')
    links = []

    for post in posts:
        link = post.find('a', href=True)
        if link:
            link_url = full_link + link['href']
            links.append(link_url)

    return links[:5]

def get_data(html):
    soup = BS(html, 'html.parser')
    container = soup.find('section', class_='product-page__purchase')
    post = container.find('div', class_='details-header')

    title = post.find('div', class_='header ng-tns-c170459131-5 ng-star-inserted').text.strip()
    genre = post.find('p', class_='category meka-font-display meka-font-display--section-label ng-star-inserted').text.strip()
    price = post.find('div', class_=' meka-price-label__price-container ').text.strip()

    data = {
        'title': title,
        'genre': genre,
        'price': price,
    }
    return data

def save_in_txt(data):
    with open('data.txt', 'a') as file:
        file.write(f"Title: {data['title']}\n")
        file.write(f"Genre: {data['genre']}\n")
        file.write(f"Price: {data['price']}\n")
        file.write('\n')

def main():
    URL = 'https://us.shop.battle.net/en-us'
    html = get_html(URL)

    # with open('battle_data.txt','w') as file:
    #     file.write("")

    if html:
        links = get_links(html)
        print("Ссылки и данные:")
        for link in links:
            post_html = get_html(link)
            if post_html:
                post_data = get_data(post_html)
                print("Link:", link)
                print("Data:", post_data)
                save_in_txt(post_data)
                print()
            else:
                print("Error in receiving HTML for a link:", link)
    else:
        print('Error in receiving HTML for main page')
        


if __name__ == '__main__':
    main()