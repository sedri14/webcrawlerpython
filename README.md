# Web Crawler CLI

## Description
This project is a web crawler command-line interface (CLI) application written in Python. The application scans a given webpage for images,
continues to every link inside that page, and scans it as well. The crawling stops once the specified depth is reached.
The results are saved in a results.json file.

## Usage
After python installation, you can run the application as follows:

```python
python crawler.py <url> <depth>
```

* `<url>`: The starting URL for the web crawler.
* `<depth>`: The maximum depth for the crawling. For example, depth=3 means the crawler can go as deep as 3 pages from the source URL, and depth=0 means only the first page is crawled.

## Results

The results are saved in a results.json file in the following format:

```json
{
    "results": [
        {
            "imageUrl": "string",
            "sourceUrl": "string",
            "depth": "number"
        }
    ]
}
```
`imageUrl`: The URL of the image found.
`sourceUrl`: The page URL where the image was found.
`depth`: The depth of the source page where the image was found.

## Requirements

* Python 3.x
* `requests` library
* `beautifulsoup4` library
* `lxml` library

You can install the required libraries using pip:
```bash
pip install requests beautifulsoup4 lxml
```

## Running the Application
1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:
   
```bash
cd <repository-directory>
```

3. Run the crawler:
   
```bash
python crawler.py <url> <depth>
```

