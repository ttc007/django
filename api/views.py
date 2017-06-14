# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from products.models import Product, Category
from api.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView,  ListAPIView
# Create your views here.

class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

@api_view(['DELETE'])
def productDelete(request, id):
    if request.method == "DELETE":
        product = Product.objects.get(pk = id)
        product.delete()
        return Response({"message": "Deleted"})
    serializer = ProductSerializers(product)
    return Response(serializer.data)

@api_view(['GET'])
def productDetail(request, p_id):
    product = Product.objects.get(pk = p_id)
    serializer = ProductSerializers(product, many = False)
    return Response(serializer.data)


@api_view(['GET'])
def products(request):
    product = Product.objects.all()
    serializer = ProductSerializers(product, many = True)
    return Response(serializer.data)

@api_view(["GET", "PUT"])
def productUpdate(request, id):
    product = Product.objects.get(pk = id)
    if request.method == "PUT":
        serializer = ProductSerializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error": serializer.errors, "error": True}) 
    serializer = ProductSerializers(product)
    return Response(serializer.data)



