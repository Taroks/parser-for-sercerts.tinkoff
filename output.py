from parser import Views
from analytics import Analytic
import pandas as pd

class preparing_to_output:
    def __init__(self):
        self.parser = Views()
        self.pages = self.parser.pages()
        self.links = self.parser.links()
        self.list_from_parser = self.parser.views()
        self.views = self.list_from_parser[0]
        self.authors = self.list_from_parser[1]
        self.analys = Analytic()
        self.result_of_comparison = self.analys.comparison(self.views)
        self.links_and_views = {}
        self.authors_and_views = []
        self.final_count_links = {}
        self.final_count_authors = []
        


    def outcome_links(self):# подготовка словаря (двумерный массив) ссылок с просмотрами выше медианы
        for link, view in list(zip(self.links, self.views)):
            self.links_and_views[link] = view 
        for key in self.links_and_views:
            if self.links_and_views[key] in self.result_of_comparison:
                value = self.links_and_views.get(key)
                self.final_count_links[key] = value
        print(len(self.final_count_links))
        return self.final_count_links

    def outcome_authors(self):# подготовка двумерного списка (словарь не терпит повторов) выше медианы
        print (self.authors, self.views, self.links)
        for i, j in zip(self.authors, self.views):
            some_list = [i,j]
            self.authors_and_views.append(some_list)   
        for k in range(len(self.authors_and_views)):
            if self.authors_and_views[k][1] in self.result_of_comparison:
                value = self.authors_and_views[k][1]
                key = self.authors_and_views[k][0]
                some_list = [key,value]
                self.final_count_authors.append(some_list)
        print(len(self.final_count_authors))
        return self.final_count_authors       

    def output(self): #формируем таблицу с данными
        i = 0
        list_of_links = []
        list_of_views = []
        list_of_authors = []
        for key in self.outcome_links():
            list_of_links.append(key)
            list_of_views.append(self.final_count_links[key])
        for key in range(len(self.outcome_authors())):
            list_of_authors.append(self.final_count_authors[key][0])
        df = pd.DataFrame({'authors':list_of_authors, 'links':list_of_links, 'views':list_of_views})
        df.to_excel('analys.xlsx', index = False)

check = preparing_to_output()
check.output()
