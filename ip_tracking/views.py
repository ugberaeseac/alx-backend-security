from django.shortcuts import render
from django.http import HttpResponse
from django_ratelimit.decorators import ratelimit

# Create your views here.


@ratelimit(key='user_or_ip', rate='10/m', method='GET', block=True)
@ratelimit(key='ip', rate='5/m', method='GET', block=True)
def home(request):
    """
    homepage
    """
    return HttpResponse('<h1>This is the Homepage!</h1>')
