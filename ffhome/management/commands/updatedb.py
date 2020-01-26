from django.core.management.base import BaseCommand
from ffhome.models import Film,Festival
from ffhome.awardsscraper import get_awards_for_all_festivals

class Command(BaseCommand):
    def handle(self,*args, **options):
        Film.objects.all().delete()

        awards = get_awards_for_all_festivals()

        for i,fest in enumerate(awards):
            print(fest)
            for film in awards[fest]:
                try:
                    f = Film(name=film.name,year=film.year,award=film.award,festival_id=i+1)
                    f.save()
                except:
                    print(f'This film could not have been saved:\n{film}')
