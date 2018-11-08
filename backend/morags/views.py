# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.core import serializers

from models import *

@method_decorator(csrf_exempt, name='dispatch')
class Lots(View):
    def post(self, request):
        #save the incoming lots
        return HttpResponse("asd")

    def get(self, request):
        data = [{
            'lot_id': 12,
            'label' : "asdasd",
            'capacity': 52
        },
        {
            'lot_id': 62,
            'label' : "lot5",
            'capacity': 527
        }]
        return JsonResponse(data, safe=False)
        data = serializers.serialize("json", ParkingLot.objects.all())
        return HttpResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class DefinePlot(View):
    def post(self, request):
        print (request.body)
        return HttpResponse("rty")

@method_decorator(csrf_exempt, name='dispatch')
class Building(View):
    def post(self, request):
        print (request.body)
        return HttpResponse("rty")