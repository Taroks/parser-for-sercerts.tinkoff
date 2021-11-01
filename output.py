from parser import Views
from analytics import Analytic
import pandas as pd

class preparing_to_output:
    links_and_views = {}
    def __init__(self):
        self.analys = Analytic()
        self.result_of_comparison = self.analys.comparison()
        self.parser = Views()
        self.links = self.parser.links()
        self.views = self.parser.views()
        self.authors = self.parser.author()
        self.final_count = {}
        self.file = open('analys.txt','w')


    def type_of_outcome(self):
        for link, view in list(zip(self.links, self.views)):
            self.links_and_views[link] = view
        for author, view in list(zip(self.authors,self.views)):
            self.authors_and_views[author] = view
        return self.links_and_views, self.authors_and_views        

    def outcome(self):
        for key in self.type_of_outcome():
            if self.links_and_views[key] in self.result_of_comparison:
                value = self.links_and_views.get(key)
                self.final_count[key] = value
        return self.final_count

    def output(self):
        i = 0
        list_of_links = []
        list_of_views = []
        self.file.write ('сортировка по медиане: \n')
        for key in self.outcome():
            # i += 1
            # line_for_output:str = str(key) + ' ; ' + 'количество просмотров: ' + str(self.final_count[key])
            # self.file.write("номер " + str(i) + ' ссылка: ' +
            #  line_for_output + '\n')
            list_of_links.append(key)
            list_of_views.append(self.final_count[key])
        df = pd.DataFrame({'links':list_of_links, 'views':list_of_views})
        df.to_excel('analys.xlsx', index = False)

check = preparing_to_output()
check.output()
