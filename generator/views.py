from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):

    return render(request, 'generator/home.html')

def about(request):
    title = 'About me'
    description = 'This is the description'

    return render(request, 'generator/about.html', {'title':title,'description':description})

def password(request):
    length = int(request.GET.get('length'))
    Characters = list('abcdefghijklmnopqrstuvwxyz')
    newPassword = ''

    if request.GET.get('uppercase'):
        Characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        Characters.extend(list('~!@#$%^&*()_+-={}[]:;>?./'))

    if request.GET.get('numbers'):
        Characters.extend(list('0123456789'))

    for x in range(length):
        newPassword += random.choice(Characters)

    return render(request, 'generator/password.html', {'password':newPassword})
