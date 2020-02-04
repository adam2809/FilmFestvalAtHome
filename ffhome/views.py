from django.http import JsonResponse
from ffhome.models import Festival,Film
import json


def get_festivals(request):
    return JsonResponse({'festivals':[f.name for f in Festival.objects.all()]})


def get_films_in_festival(request,fest_id):
    films = Film.objects.filter(festival_id=fest_id)
    return JsonResponse({'films':[{'name':f.name,'year':f.year,'award':f.award} for f in films]})


def testing(request):
    with open('ffhome/testJustwatchResponse.json') as f:
        j = json.loads(f.read())
    return JsonResponse(j)
