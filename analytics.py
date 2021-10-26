from parser import Views

class Analytic:

    def __init__(self):
        self.views = Views()
        self.list_of_views = self.views.views()
        self.top_of_views = []
        self.median = self.median()

    def median(self):
        self.list_of_views.sort()
        median = self.list_of_views[len(self.list_of_views)//2]
        return median

    def comparison(self):
        for item in self.list_of_views:
            if item >= self.median:
                self.top_of_views.append(item)
        return self.top_of_views

# check = Analytic()
# check.comparison()
# print("медиана:", self.median, '\n', 
# 'всё что выше медианы:', check.comparison(), '\n',
# 'кол-во элементов:', len(check.top_of_views))