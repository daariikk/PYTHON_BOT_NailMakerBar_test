from typing import Dict
import requests
from bs4 import BeautifulSoup

def _make_response() -> Dict:

    """Функция, которая парсит прайс-лист с сайта NailMakerBar"""

    url = 'https://nailmaker.bar/price/'
    info_date = dict()

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    sections = soup.find_all('div', class_='prices-item')

    for section in sections:
        title = section.find('h2', class_='prices-item_title').text.strip()

        info_date[title] = dict()
        info_element = section.find_all('div', class_='question-title')

        for info in info_element:
            name_service = info.contents[0].strip()
            #print(f'name_service = {name_service}')
            price_service = info.find('span', class_='text-price').text.strip()
            #print(f'price_service = {price_service}')
            info_date[title][name_service] = price_service

    return info_date







        