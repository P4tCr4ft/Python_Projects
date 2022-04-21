# not sure where below line came from ..?
# So this is require when using templates

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

'''
Below the index view/function shows simple response (1st return statement), then some HTML with
a link to the rango about view/function (2nd return statement).
And 3rdly shows use of templates
'''

def index(request):
    # return HttpResponse('Rango says hey there partner!')

    # return HttpResponse(
    #     '''<p>Rango says hey there partner!</p>
    #     <p>Here's a link to <a href='http://localhost:8000/rango/about'> about page </a></p>'''
    # )

    '''Construct a dictionary to pass to the template engine as it's context.
    Note: the key boldmessage is the same as {{ boldmessage }} in the template'''

    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

def about(request):
    return HttpResponse('Rango says here is the about info...')
