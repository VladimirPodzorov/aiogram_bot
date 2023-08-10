import requests
from bs4 import BeautifulSoup as b


def hollyd_pars():
    req_url = requests.get('https://sptoday.ru/kakoj-segodnya-prazdnik/')
    soup = b(req_url.text, 'html.parser')
    holiday = soup.find_all('div', class_="prazdnik")
    holday = [i.text.split('\n') for i in holiday]
    for i_day in holday:
        if isinstance(i_day, list):
            return i_day[13]


if __name__ == '__main__':
    hollyd_pars()
