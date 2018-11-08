# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class Lots(View):
    def post(self, request):
        #save the incoming lots
        return HttpResponse("asd")

    def get(self, request):
        return HttpResponse("qwe")