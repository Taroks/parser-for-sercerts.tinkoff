from parser import Views

class Analytic():
    def __init__(self):
        self.top_of_views = []

    def median(self,list_of_views):# считаем медиану
        print ('_'* 70,'function median','_'*69)
        list_of_views.sort()
        median = list_of_views[len(list_of_views)//2]
        return median

    def comparison(self, list_of_views):#режем просмотры по медиане, из всего что выше формируем новый
        print ( '_'* 70,'function comparison','_'*65)
        median = self.median(list_of_views)
        for item in list_of_views:
            if item >= median:
                self.top_of_views.append(item)
        return self.top_of_views
