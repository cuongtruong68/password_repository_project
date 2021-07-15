# from typing_extensions import runtime
from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html')
def about(request):
    return render(request,'generator/about.html')

def password(request):

    character = list('hdhdiouu9028bjfdbnjkdjj')
    if request.GET.get('uppercase'):
        character.extend(list('ABC'))
    if request.GET.get('special'):
        character.extend(list('!@#'))
    if request.GET.get('number'):
        character.extend('123456')
    
    
    length = int(request.GET.get('length', 12))
    thepassword =''
    for x in range(length):
        thepassword += random.choice(character)
    return render(request,'generator/password.html', {'password':thepassword})