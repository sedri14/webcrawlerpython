from bs4 import BeautifulSoup
import requests

URL = 'https://en.wikipedia.org/wiki/Cat'


def get_data(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    return soup


def print_images(soup):
    images = soup.findAll('img')
    for img in images:
        print(img)


def scrape():
    soup = get_data(URL)
    print_images(soup)


if __name__ == '__main__':
    scrape()
    print('finished')
