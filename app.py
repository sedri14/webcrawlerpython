from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import json
import argparse

visited_urls = set()


def get_data(url):
    try:
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')
        return soup
    except requests.exceptions.RequestException as e:
        print(f'Failed to fetch {url}')
        return None


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
        print(img_data)


def scrape(url, cur_depth, limit_depth, image_data_list):
    if limit_depth == 0 or cur_depth == limit_depth:
        soup = get_data(url)
        if soup:
            extract_images(soup, url, limit_depth, image_data_list)
        return

    soup = get_data(url)
    if soup:
        extract_images(soup, url, cur_depth, image_data_list)

    # get all links in page
    links = soup.findAll('a')
    for link in links:
        relative_url = link['href']
        absolute_url = urljoin(url, relative_url)
        if absolute_url not in visited_urls:
            visited_urls.add(absolute_url)
            scrape(absolute_url, cur_depth + 1, limit_depth, image_data_list)


def main():
    parser = argparse.ArgumentParser(description="Web Crawler")
    parser.add_argument("url", type=str, help="Url")
    parser.add_argument("depth", type=int, help="Depth")
    args = parser.parse_args()

    img_data_list = []
    scrape(args.url, 0, args.depth, img_data_list)

    # write results to a json file
    data_to_save = {
        "results": img_data_list
    }
    with open('results.json', 'w') as json_file:
        json.dump(data_to_save, json_file, indent=4)


if __name__ == "__main__":
    main()
