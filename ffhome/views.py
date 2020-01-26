from django.http import JsonResponse
from ffhome.models import Festival,Film

def get_festivals(request):
    return JsonResponse({'festivals':[f.name for f in Festival.objects.all()]})


def get_films_in_festival_by_year(request,name,year):
    fest = Festival.objects.get(name=name)
    films = Film.objects.filter(festival_id=fest.id).filter(year=year)
    return JsonResponse({'films':[{'name':f.name,'year':f.year,'award':f.award} for f in films]})



def get_streaming_services(request):
    pass
