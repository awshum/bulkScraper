import csv
import requests
from bs4 import BeautifulSoup

def scrapeUrl(url, selector):
    #diccnt
    response = requests.get(url)
    print('[{status_code}] Sending GET request to: {url}.'.format(
        status_code=response.status_code, url=url))
    soup = BeautifulSoup(response.content.decode('utf-8'), 'lxml')
    element = soup.select(selector)
    if len(element) > 1:
        print(len(element))
        print('Found multiple matches for a single URL: ')
        for n, e in enumerate(element):
            print(str(n) + ") " + str(e))
        keep = int(input('Which do you want to keep? '))
        return element[keep].text.replace("\\r\\n", " ")
    else:
        if len(element) == 0:
            return ""
        return element[0].text.replace("\r\n", " ")


def main():
    print("----------"*10)
    print("""This script will allow you to scrape a single css selector 
            off every URL provided in txt file.""")
    print("----------"*10)
    file_path = input("Please input your file path: ")
    css_selector = input("Please input css selector: ")
    with open(file_path) as f:
        urls = f.readlines()
    texts = []
    for url in urls:
        texts.append((url.rstrip('\n'), scrapeUrl(url.rstrip('\n'), css_selector)))
    print(texts)
    output_path = input("Please provide a path or filename for output: ")
    with open(output_path, 'w') as output:
        csv_writer = csv.writer(output, delimiter=';')
        for row in texts:
            csv_writer.writerow(row)

if __name__ == "__main__":
    main()
