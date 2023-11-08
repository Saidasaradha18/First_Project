from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def JamPandu(request):
    return HttpResponse('<h1><marquee>Hey Guys How Are You<h1><marquee>')

def JigelRani(reguest):
    return HttpResponse('<h1><marquee>Iam Fine JamPandu<h1><marquee>')

def ChittiBabu(reqhuest):
    return HttpResponse('<h1><marquee>Iam also Fine JamPandu, Thank U For Asking<h1><marquee>')