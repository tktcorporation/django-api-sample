from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View


class TestApiView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"})
