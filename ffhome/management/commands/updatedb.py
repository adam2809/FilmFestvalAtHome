from django.core.management.base import BaseCommand
from ffhome.models import Film,Festival
from ffhome.awardsscraper import get_awards_for_all_festivals

class Command(BaseCommand):
    def handle(self,*args, **options):
        self.updateFestivals()
        self.updateFilms()


    def updateFestivals(self):
        Festival.objects.all().delete()

        for fest_name in ['Academy Awards - OSCARS',
                          'Australian Film Institute Awards',
                          'BAFTA Film Awards',
                          'CESAR Film Awards',
                          'Berlin International Film Festival',
                          'Golden Globe Awards',
                          'Venice International Film Festival',
                          'Cannes International Film Festival',
                          'Sundance Film Festival',
                         ]:


            try:
                Festival(name=fest_name).save()
            except Exception as e:
                print(f'Could not save {fest_name}\nThe exception was:\n')
                print(e)

    def updateFilms(self):
        Film.objects.all().delete()

        awards = get_awards_for_all_festivals()
        print(awards)

        for i,fest in enumerate(awards):
            print(fest)
            for film in awards[fest]:
                try:
                    f = Film(name=film.name,year=film.year,award=film.award,festival_id=i+1)
                    f.save()
                except Exception as e:
                    print(f'This film could not have been saved:\n{film}\nThe exception was:\n')
                    print(e)
