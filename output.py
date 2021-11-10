from parser import Views
from analytics import Analytic
import pandas as pd

class preparing_to_output:
    def __init__(self):
        self.parser = Views()
        self.links = self.parser.links()
        self.views = self.parser.views()
        self.authors = self.parser.author()
        self.analys = Analytic()
        self.result_of_comparison = self.analys.comparison()
        self.links_and_views = {}
        self.authors_and_views = []
        self.final_count_links = {}
        self.final_count_authors = {}


    def type_of_outcome_links(self):
        for link, view in list(zip(self.links, self.views)):
            self.links_and_views[link] = view
        return self.links_and_views

    def type_of_outcome_authors(self):
        authors = []
        views = []
        a = dict(zip(self.views, self.authors))
        print (len(self.authors), len(self.views), len(a))
        # for author, view in list(zip(self.authors,self.views)):
        #     print (author, ":", view)
        #     authors.append(author)
        #     views.append(view)
        #     print (len(authors), len(views))
        for i,j in list(zip(authors,views)):
                self.authors_and_views.append(list.append(i,j))
        print(self.authors_and_views)
        # print (self.authors_and_views)
        return self.authors_and_views        

    def outcome_links(self):
        for key in self.type_of_outcome_links():
            if self.links_and_views[key] in self.result_of_comparison:
                value = self.links_and_views.get(key)
                self.final_count_links[key] = value
        return self.final_count_links

    def outcome_authors(self):
        for key in self.type_of_outcome_authors():
            if self.authors_and_views[key] in self.result_of_comparison:
                value = self.authors_and_views.get(key)
                self.final_count_authors[key] = value
        return self.final_count_authors
        

    def output(self):
        i = 0
        list_of_links = []
        list_of_views = []
        list_of_authors = []
        for key in self.outcome_links():
            list_of_links.append(key)
            list_of_views.append(self.final_count_links[key])
        for key in self.outcome_authors():
            list_of_authors.append(key)
        # df = pd.DataFrame({'authors':list_of_authors, 'links':list_of_links, 'views':list_of_views})
        # df.to_excel('analys.xlsx', index = False)

check = preparing_to_output()
check.output()
