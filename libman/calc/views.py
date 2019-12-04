# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("Hello World")
    return render(request, 'home.html', {'name':'Siddharth'})


def add(request):
    var1 = request.POST['num1']
    var2 = request.POST['num2']

    res = int(var1) + int(var2)

    return render(request, 'result.html', {'result': res})