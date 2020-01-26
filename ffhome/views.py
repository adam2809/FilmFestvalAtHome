from django.http import JsonResponse
from ffhome.models import Festival,Film

def get_festivals(request):
    return JsonResponse({'festivals':[f.name for f in Festival.objects.all()]})


def get_films_in_festival_by_year(request,name,year):
    print(name)
    fest = Festival.objects.get(name=name)
    films = Film.objects.get(year=year,festival_id=fest.id)
    return JsonResponse({'films':[f.name for f in films]})



def get_streaming_services(request):
    pass
