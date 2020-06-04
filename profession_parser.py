from time import sleep
import requests as req
import json
from pathlib import Path
import os.path
from bs4 import BeautifulSoup

file = Path('data.txt')
if file.is_file():
    print("File is already exist")
    if os.path.getsize('data.txt') == 0:
        print("Seems like file is empty...")
        print("Starting parsing professions...")
        print("Its takes a few minutes...")
        url = "https://www.ucheba.ru/prof/search"

        with req.Session() as se:
            se.headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6"
            }

            resp = se.get(url)

        index = BeautifulSoup(resp.content, "html.parser")
        pages = []
        profs = {}
        profs_description = []

        for x in range(0, 13):
            print(f"Fetching data from https://www.ucheba.ru/prof/search?s={x * 20}")
            sleep(3)
            pages.append(se.get(f"https://www.ucheba.ru/prof/search?s={x * 20}"))

        print(f"Fetching data from https://www.ucheba.ru/prof/? is completed")

        for sort in pages:
            pars = BeautifulSoup(sort.content, 'html.parser')

            for el in pars.select('.pl-item.col-lg-3.col-sm-4.mb-section'):
                link = el.find('a')
                try:
                    profs[link.get('title')] = link.get('href')
                except AttributeError as error:
                    print("Error - ", error)

        pages = []

        for prof in profs.keys():
            print(f"Fetching data from https://www.ucheba.ru{profs.get(prof)}")
            sleep(3)
            pages.append(se.get(f"https://www.ucheba.ru{profs.get(prof)}"))

        print(f"Fetching data from https://www.ucheba.ru/prof is completed")
        print(f"Starting merging...")

        for sort in pages:
            pars = BeautifulSoup(sort.content, 'html.parser')

            for el in pars.select(".head-announce__lead"):
                profs_description.append(el.get_text(strip=True))

        for i, prof in enumerate(profs.keys()):
            profs[prof] = profs_description[i]

        with open('data.txt', 'w') as outfile:
            json.dump(profs, outfile)

        print(f"Merging is completed!")
    else:
        print("File is not empty, operation of parsing professions will be skipped")
        exit(0)