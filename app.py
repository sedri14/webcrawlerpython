from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

URL = 'https://www.geeksforgeeks.org/image-scraping-with-python/'


def get_data(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    return soup


def print_images(soup, source_url, depth):
    images = soup.findAll('img')
    for img in images:
        img_url = img.get('src')
        print(f'sourceUrl: {source_url}')
        print(f'imageUrl: {img_url}')
        print(f'depth: {depth}')
        print('******************************')


def scrape(url, cur_depth, limit_depth):
    if limit_depth == 0 or cur_depth == limit_depth:
        soup = get_data(url)
        print_images(soup, url, limit_depth)
        return

    soup = get_data(url)
    print_images(soup, url, cur_depth)

    # get all links in page
    links = soup.findAll('a')
    for link in links:
        relative_url = link['href']
        absolute_url = urljoin(url, relative_url)
        scrape(absolute_url, cur_depth + 1, limit_depth)


if __name__ == '__main__':

    scrape(URL, 0, 1)
    print('finished')
