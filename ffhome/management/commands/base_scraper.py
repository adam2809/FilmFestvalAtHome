class Film:
    def __init__(self,name,award,year):
        self.name = name
        self.award = award
        self.year = year

    def __str___(self):
        return f'name={self.name}\taward={self.award}\tyear={self.year}'

class BaseScraper:
    # Should return a dict where keys are full names of festivals and values are lists of films of type Film defined above for each festtival
    def scrape():
        pass
