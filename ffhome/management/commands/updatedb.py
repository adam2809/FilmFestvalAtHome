from ffhome.management.commands.scrapers.awardsscraper import NetogramScraper
from django.core.management.base import BaseCommand
from ffhome.models import Film,Festival

class Command(BaseCommand):
    film_id = 1

    def handle(self,*args, **options):
        Festival.objects.all().delete()
        Film.objects.all().delete()

        for scraper in [NetogramScraper()]:
            self.update(scraper)

    def update(self,scraper):
        festFilmDict = scraper.scrape()

        for i,fest in enumerate(festFilmDict):
            Festival(id=i+1,name=fest).save()

            for film in festFilmDict[fest]:
                try:
                    f = Film(id=self.film_id,
                             name=film.name,
                             year=film.year,
                             award=film.award,
                             festival_id=i+1).save()
                    self.film_id+=1
                except Exception as e:
                    print(f'This film could not have been saved:\n{film}\nThe exception was:')
                    print(e)
