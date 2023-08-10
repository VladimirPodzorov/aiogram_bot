import requests
from bs4 import BeautifulSoup as b


def jokas_pars():
    req_url = requests.get('https://www.anekdot.ru/random/anekdot/')
    soup = b(req_url.text, 'html.parser')
    anekdots = soup.find_all('div', class_="text")
    return [i.text for i in anekdots]


if __name__ == '__main__':
    jokas_pars()
