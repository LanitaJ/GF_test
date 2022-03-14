import requests
from bs4 import BeautifulSoup



def soup_connection(link):
    res = requests.get(link, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}, verify=False)
    html = BeautifulSoup(res.text, 'html.parser')
    return html