# not sure where below line came from ...
# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    # return HttpResponse('Rango says hey there partner!')
    return HttpResponse(
        '''<p>Rango says hey there partner!</p>
        <p>Here's a link to <a href='http://localhost:8000/rango/about'> about page </a></p>'''
    )

def about(request):
    return HttpResponse('Rango says here is the about info...')
