from django.core.management.base import BaseCommand
from ffhome.models import Film,Festival
from ffhome.awardsscraper import get_awards_for_all_festivals

class Command(BaseCommand):
    def handle(self,*args, **options):
        self.updateFestivals()
        self.updateFilms()


    def updateFestivals(self):
        Festival.objects.all().delete()

        for i,fest_name in enumerate(
                         ['Academy Awards - OSCARS',
                          'Australian Film Institute Awards',
                          'BAFTA Film Awards',
                          'CESAR Film Awards',
                          'Berlin International Film Festival',
                          'Golden Globe Awards',
                          'Venice International Film Festival',
                          'Cannes International Film Festival',
                          'Sundance Film Festival',
                         ]):


            try:
                Festival(id=i+1,name=fest_name).save()
            except Exception as e:
                print(f'Could not save festival {fest_name}\nThe exception was:\n')
                print(e)

    def updateFilms(self):
        Film.objects.all().delete()

        awards = get_awards_for_all_festivals()

        saved_films_count = 0

        for i,fest in enumerate(awards):
            for film in awards[fest]:
                try:
                    f = Film(id=saved_films_count+1,name=film.name,year=film.year,award=film.award,festival_id=i+1)
                    f.save()
                    saved_films_count+=1
                except Exception as e:
                    print(f'This film could not have been saved:\n{film}\nThe exception was:')
                    print(e)
