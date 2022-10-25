from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def hello(request, *args, **kwargs):
    return JsonResponse({"message":"hello!!"})



    