from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# class JsonResponse(data, encoder=DjangoJSONEncoder, safe=True, json_dumps_params=None, **kwargs)[source]¶

# Create your views here.
def index(request):
  return HttpResponse("Hello World. You're at the polls index")

def scraper(request, username):
  #  process the data - pass username to a function elsewhere that (constructs the url, scrapes the url, passes to the api, receives the data which has been sentiment analyzed, then passes the relevant part of that info back here)
  #
  return JsonResponse({});
