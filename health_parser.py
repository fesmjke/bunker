import json
import requests as req
from bs4 import BeautifulSoup
from pathlib import Path
import os.path

file = Path('diseases.txt')
if file.is_file():
    print("File is already exist")
    if os.path.getsize('diseases.txt') == 0:
        url = "http://minzdrav.gov.by/ru/dlya-belorusskikh-grazhdan/bolezni-ot-a-do-ya/"

        with req.Session() as se:
            se.headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6"
            }
            resp = se.get(url)

        diseases = {}

        index = BeautifulSoup(resp.content, "html.parser")

        for el in index.select('section.news-list-page.rnpc div.row div.col-md-4 '):
            try:
                diseases[el.get_text()] = "description none"
            except AttributeError as error:
                print("Error - ", error)

        with open('diseases.txt', 'w') as outfile:
            json.dump(diseases, outfile)
    else:
        exit(0)