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
        self.links_and_views = {}
        self.prepared_list = []
        self.final_count_links = []
        self.final_count_authors = []
        self.final_count = []


    def Final_count(self, views, some_list) -> list:
        analys = Analytic()
        result_of_comparison = analys.comparison(self.views)
        self.final_count = []
        some_list_1 = []
        for k in range(len(some_list)):
            if some_list[k][1] in result_of_comparison:
                value = some_list[k][1]
                key = some_list [k][0]
                some_list_1 = [key,value]
                self.final_count.append(some_list_1)
        print ("Значение переменных интуресющих тебя :", key, value)
        return self.final_count

    def preparing_of_lists(self, some_list, views) -> list:
        some_list_1 = []
        self.prepared_list = []
        for i, j in zip(some_list, views):
            some_list_1 = [i,j]
            self.prepared_list.append(some_list_1)
        return self.prepared_list

    def output(self): #формируем таблицу с данными
        list_of_links = []
        list_of_views = []
        list_of_authors = []
        prepared_list_of_links = self.preparing_of_lists(self.links, self.views)
        prepared_list_of_authors = self.preparing_of_lists(self.authors, self.views)
        self.final_count_links = self.Final_count(self.views,prepared_list_of_links)
        self.final_count_authors = self.Final_count(self.views, prepared_list_of_authors)
        for key in range(len(self.final_count_links)):
            list_of_links.append(self.final_count_links[key][0])
            list_of_views.append(self.final_count_links[key][1])
        for key in range(len(self.final_count_authors)):
            list_of_authors.append(self.final_count_authors[key][0])
        df = pd.DataFrame({'authors':list_of_authors, 'links':list_of_links, 'views':list_of_views})
        df.to_excel('analys.xlsx', index = False)

check = preparing_to_output()
check.output()
