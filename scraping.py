import re
import connector

SOUP = connector.soup_connection('https://kwork.ru/projects')

def scrap_name():
    names = []
    for name_code in SOUP.find_all('div', class_='wants-card__header-title first-letter breakwords pr250'):
        name = name_code.find('a')
        names.append(name.text)
    return names


def scrap_first_price():
    prices = []
    for price_code in SOUP.find_all('div', class_='wants-card__header-price wants-card__price m-hidden'):
        price = price_code.find('span')
        prices.append(price.text)
    return prices

def scrap_second_price():
    prices = []
    for price_code in SOUP.find_all('div', class_='wants-card__description-higher-price'):
        price = price_code('span')
        prices.append(price.text)
    return prices

def scrap_details():
    details = []
    for detail_code in SOUP.find_all('div', class_='breakwords first-letter js-want-block-toggle js-want-block-toggle-full hidden'):
        details.append(detail_code.text)
    return details




