import requests
from bs4 import BeautifulSoup
from lxml import html
import re
import time

class Views:
    def __init__(self):
        self.list_of_links=[]
        self.list_of_pages = ['https://secrets.tinkoff.ru/novosti/']
        self.list_of_views = []
        self.list_of_authors = []

    def connection (self,link):
        while True:
            try:
                request = requests.get(link)
                break
            except Exception as e:
                time.sleep(5)
                continue
        return request


    def links (self):
        print ( '_'* 70,'function links','_'*70)
        if len(self.list_of_links) == 0:
            for page in self.pages():
                r = self.connection(page)
                req = r.text
                soup = BeautifulSoup(req, 'lxml')
                for link in soup.main.section.find_all('a'):
                    rigth_links = re.findall(r'novosti', str(link))
                    if len(rigth_links) == 1:
                        self.list_of_links.append(link.get('href'))
        return self.list_of_links

    def pages (self):
        print ( '_'* 70,'function pages','_'*70)
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
        print ( '_'* 70,'function views','_'*70)
        for link in self.links():
            r = self.connection(link)
            req = r.text
            soup = BeautifulSoup(req,'lxml')
            count_of_views = str(soup.find('span', {'class': "post-views-count"}))
            result = re.findall(r'\d+', count_of_views)
            if len(result) != 0:
                if len(result) < 2:
                    self.list_of_views.append(int(result[0]))
                else:
                    self.list_of_views.append(int(result[0] + result[1]))
        return self.list_of_views

    def author(self):
        print ( '_'* 70,'function author','_'*70)
        a = 0
        for link in self.list_of_links:
            r = self.connection(link)
            req = r.text
            soup = BeautifulSoup(req,'lxml')
            author_str = str(soup.find('span', {'class': "details__editor"}))
            left_author = re.split(r'>', author_str)
            only_author = re.split(r'<', left_author[1])
            self.list_of_authors.append(only_author[0])
        return self.list_of_authors

        

        


# check = Views()
# links = check.views()
# authors = check.author()
# print(links, '\n', len(links), "\n", authors, len(authors))
