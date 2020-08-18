from urllib.request import urlopen


import urllib
import requests
from django.contrib.auth.models import User
from django.shortcuts import render


def home(request):
    response = requests.get('http://echo.jsontest.com/insert-key-here/insert-value-here/key/value')
    data = response.json()
    return render(request, 'index.html', {
        'sEndpoint': data['insert-key-here'],
        'iSession': data['key']
    })


def userprocess(request):
    values = {
     'sEmail': 'oguzhan.ztrk14@gmail.com',
     'sPwd': '12345'}
    #user = User.objects.create_user('Oğuzhan','oguzhan.ztrk14@gmail.com','12345')
    #user = User.objects.values('Görkem')
   # result = urlopen('https://secure.logmeinrescue.com/api/',urllib)
    #content = result.read()
    values = {
        'sEmail': 'oguzhan.ztrk14@gmail.com',
        'sPwd': '12345'}
    return render(request, 'index.html', {
     #   content
    })

