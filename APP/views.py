from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def first(request):
    return HttpResponse('<h1> This is First Function </h1>')

def second(request):
    return HttpResponse('<marquee><h1> This is Second Function </h1></marquee>')

def third(request):
    return HttpResponse('<h1> This is Third Function </h1>')

def fourth(request):
    return HttpResponse('<marquee><h1> This is Fourth Function </h1></marquee>')

def fifth(request):
    return HttpResponse('<h1> This is Fifth Function </h1>')

def sixth(request):
    return HttpResponse('<marquee><h1> This is Sixth Function </h1></marquee>')

def seventh(request):
    return HttpResponse('<h1> Hey.....I Am Shubham Bharti!!!!!!!!!! </h1>')
