from django.http import JsonResponse,HttpResponse,HttpResponseNotFound
from ffhome.models import Festival,Film
from datadog import statsd
import json


def get_festivals(request):
    statsd.increment('festival_requests',tags=["environment:dev"])
    return JsonResponse({'festivals':[f.name for f in Festival.objects.all()]})


def get_films_in_festival(request,fest_id):
    statsd.increment('film_requests',tags=["environment:dev"])
    films = Film.objects.filter(festival_id=fest_id)
    return JsonResponse({'films':[{'name':f.name,'year':f.year,'award':f.award} for f in films]})


def jw_query_metrics(request,hit_or_miss):
    print(hit_or_miss)
    if hit_or_miss == 'hit':
        statsd.increment('jw_query.hit')
        return HttpResponse()

    if hit_or_miss == 'miss':
        statsd.increment('jw_query.miss')
        return HttpResponse()

    return HttpResponseNotFound()
