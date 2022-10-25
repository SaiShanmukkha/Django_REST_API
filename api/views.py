from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json, traceback
from api.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(["GET", "POST"])
def hello(request, *args, **kwargs):
    product_model_data = Product.objects.all().order_by("?").first()
    return Response(model_to_dict(product_model_data))



    