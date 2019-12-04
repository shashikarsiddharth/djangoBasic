# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def index(request):
    #return HttpResponse("Hello World")
    # dest1 = Destination()
    # dest1.id = 1
    # dest1.name = "Indonesia"
    # dest1.price = 1400
    # dest1.desc = "Fast and Furious City"
    # dest1.img = 'destination_1.jpg'
    # dest1.offer = True
    
    # dest2 = Destination()
    # dest2.id = 2
    # dest2.name = "New Zealand"
    # dest2.price = 1100
    # dest2.desc = "Green City"
    # dest2.img = 'destination_2.jpg'
    # dest2.offer = False

    # dest3 = Destination()
    # dest3.id = 3
    # dest3.name = "Brazil"
    # dest3.price = 1600
    # dest3.desc = "Land of Champs"
    # dest3.img = 'destination_3.jpg'
    # dest3.offer = False

    # dest4 = Destination()
    # dest4.id = 4
    # dest4.name = "Australia"
    # dest4.price = 2400
    # dest4.desc = "Nature at it's best"
    # dest4.img = 'destination_4.jpg'
    # dest4.offer = False

    # dest5 = Destination()
    # dest5.id = 5
    # dest5.name = "Sri Lanka"
    # dest5.price = 200
    # dest5.desc = "The Golden City"
    # dest5.img = 'destination_5.jpg'
    # dest5.offer = False

    # dest6 = Destination()
    # dest6.id = 6
    # dest6.name = "Turkey"
    # dest6.price = 1300
    # dest6.desc = "Turkish Delights"
    # dest6.img = 'destination_6.jpg'
    # dest6.offer = True
    # dests = [dest1, dest2, dest3, dest4, dest5, dest6]

    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests': dests})

