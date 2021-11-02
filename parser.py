import requests
from bs4 import BeautifulSoup
from lxml import html
import re
import time
import logging


class Views:
    def __init__(self):
        self.list_of_links=[]
        self.list_of_pages = ['https://secrets.tinkoff.ru/novosti/']
        self.list_of_views = []
        self.list_of_authors = []

    def links (self):
        if len(self.list_of_links) == 0:
            for page in self.pages():
                req = requests.get(page).text
                soup = BeautifulSoup(req, 'lxml')
                for link in soup.main.section.find_all('a'):
                    rigth_links = re.findall(r'novosti', str(link))
                    if len(rigth_links) == 1:
                        self.list_of_links.append(link.get('href'))
        return self.list_of_links

    def pages (self):
        num = 1
        req = requests.get('https://secrets.tinkoff.ru/novosti/page/2/').text
        soup = BeautifulSoup(req,'lxml')
        count_of_pages = str(soup.head.find_all(re.compile('title')))
        numbers = re.split(r'из', count_of_pages)
        last_page = re.split(r'<', numbers[1])
        while num < int(last_page[0]):
            num += 1
            page = f'https://secrets.tinkoff.ru/novosti/page/{num}/'
            self.list_of_pages.append(page)
        return self.list_of_pages
        
    def views(self):
        counter: int = 0
        for link in self.links():
            while True:
                try:
                    r = requests.get(link)
                    if r.status_code != 200:
                        logging.info("Ошибка, Код ответа: %s", r.status)
                        time.sleep(1)
                        continue
                    req = r.text
                    soup = BeautifulSoup(req,'lxml')
                    count_of_views = str(soup.find('span', {'class': "post-views-count"}))
                    result = re.findall(r'\d+', count_of_views)
                    if len(result) != 0:
                        if len(result) < 2:
                            self.list_of_views.append(int(result[0]))
                        else:
                            self.list_of_views.append(int(result[0] + result[1]))
                    counter += 1
                    print('!'*20, "counter:", counter, '!'*20, r.status_code)
                    if counter == len(self.list_of_links):
                        break
                except Exception as e:
                    print(type(e), '\nstatus code: ',r.status_code)
                    time.sleep(1)
        return self.list_of_views

    def author(self):
        a = 0
        for link in self.list_of_links:
            req = requests.get(link).text
            soup = BeautifulSoup(req,'lxml')
            author_str = str(soup.find('span', {'class': "details__editor"}))
            left_author = re.split(r'>', author_str)
            only_author = re.split(r'<', left_author[1])
            self.list_of_authors.append(only_author[0])
        return self.list_of_authors

        

        


# check = Views()
# check.views()
# print(check.views())
