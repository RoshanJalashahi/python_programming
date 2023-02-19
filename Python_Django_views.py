'''
Django views are Python functions that takes http requests and returns http response, like HTML documents.

A web page that uses Django is full of views with different tasks and missions.

Views are usually put in a file called views.py located on your app's folder.

There is a views.py in your members folder that looks like this:
'''


'''
Find it and open it, and replace the content with this:

my_tennis_club/members/views.py:

from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")'''