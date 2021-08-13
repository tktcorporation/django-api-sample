from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

class TestApiView(View):

    def get(self, request):
        return JsonResponse({'status': 'ok'})
