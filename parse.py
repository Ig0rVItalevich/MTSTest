import re
import time
import json
import configparser

import requests
from bs4 import BeautifulSoup

config = configparser.ConfigParser()
config.read("config.ini")

FIRST_PAGE = 1
LAST_PAGE = 20

def parse(films):
    headers = {
        "Accept": config["HEADERS"]["Accept"], 
        "Accept-encoding": config["HEADERS"]["Accept-encoding"],
        "Accept-language": config["HEADERS"]["Accept-language"],
        "Cache-control": config["HEADERS"]["Cache-control"],
        "Cookie": config["HEADERS"]["Cookie"],
        "User-agent": config["HEADERS"]["User-agent"]
    }
    
    for page in range(FIRST_PAGE, LAST_PAGE + 1):
        url = f'https://www.kinopoisk.ru/lists/movies/popular/?page={page}'
        r = requests.get(url=url, headers=headers)

        parse_page(films, r.text)

        time.sleep(5)


def parse_page(films, page):
    soup = BeautifulSoup(page, "html.parser")
    for record in soup.find_all(attrs={'class': 'styles_root__ti07r'}, recursive=True):
        film = {}
        film['position'] = check_none(record.find(
            attrs={'class': 'styles_position__TDe4E'}, recursive=True))
        film['rating'] = check_none(record.find(
            attrs={'class': 'styles_kinopoiskValue__9qXjg'}, recursive=True))
        film['title_russian'] = check_none(record.find(
            attrs={'class': 'styles_mainTitle__IFQyZ'}, recursive=True))
        film['title_english'] = check_none(record.find(
            attrs={'class': 'desktop-list-main-info_secondaryTitle__ighTt'}, recursive=True))
        film['year'] = check_none(record.find(
            attrs={'class': 'desktop-list-main-info_secondaryText__M_aus'}, recursive=True))
        if film['year'] != "-":
            film['year'] = re.search(r"\d{4}", film['year'])
            if film['year'] is None:
                film['year'] = "-"
            else:
                film['year'] = film['year'].group(0)

        films.append(film)


def check_none(field):
    if field is None:
        field = "-"
    else:
        field = field.getText()

    return field


if __name__ == "__main__":
    films = []
    parse(films)

    with open("items.json", "w") as write_file:
        json.dump(films, write_file, indent=4, separators=(',', ': '))
