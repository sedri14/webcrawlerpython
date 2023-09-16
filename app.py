from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import json


URL = 'https://www.geeksforgeeks.org/image-scraping-with-python/'


def get_data(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    return soup


def extract_images(soup, source_url, depth, image_data_list):
    images = soup.findAll('img')
    for img in images:
        img_url = img.get('src')
        img_data = {
            "sourceUrl": source_url,
            "imageUrl": img_url,
            "depth": depth
        }
        image_data_list.append(img_data)


def scrape(url, cur_depth, limit_depth, image_data_list):
    if limit_depth == 0 or cur_depth == limit_depth:
        soup = get_data(url)
        extract_images(soup, url, limit_depth, image_data_list)
        return

    soup = get_data(url)
    extract_images(soup, url, cur_depth, image_data_list)

    # get all links in page
    links = soup.findAll('a')
    for link in links:
        relative_url = link['href']
        absolute_url = urljoin(url, relative_url)
        # todo: check for previously visited urls
        scrape(absolute_url, cur_depth + 1, limit_depth, image_data_list)


if __name__ == '__main__':
    img_data_list = []
    scrape(URL, 0, 1, img_data_list)

    # write results to a json file
    data_to_save = {
        "results": img_data_list
    }
    with open('results.json', 'w') as json_file:
        json.dump(data_to_save, json_file, indent=4)
    print('finished')
