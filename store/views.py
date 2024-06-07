from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView, ListAPIView
from .models import Product, Customer
from .serializers import ProductSerializer, CustomerSerializer
# Create your views here.

@api_view(['GET',"POST"])
def product_list(req):
    if req.method =='GET':
       queryset = Product.objects.select_related('collection').all()
       serializer = ProductSerializer(queryset, many=True, context={'request':req}) 
       return Response(serializer.data)
    elif req.method == 'POST':
        serializer = ProductSerializer(data=req.data)
        # if serializer.is_valid():
        #     serializer.validated_data
        #     return Response('ok')
        # else:
        #     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        serializer.save()
        return Response(serializer.data)

# * One version for getting object 
# @api_view() 
# def singleProduct(req, id):
#     try:
#         product = Product.objects.get(pk=id)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     except Product.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['GET',"PATCH","DELETE"])
def single_product(req, id):
    if req.method =='GET':
       product = get_object_or_404(Product, pk=id)
       serializer = ProductSerializer(product)
       return Response(serializer.data)
    elif req.method == 'PUT':
        serializer = ProductSerializer(product,data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif req.method == 'DELETE':
        if product.orderitem_set.count()>0:
            return Response({'error':'Product cannot be deleted'})
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view()
def collection_details(req,pk):
    return Response("ok")

@api_view(['GET','PATCH','DELETE'])
def store_customer(req,id):
    customer = get_object_or_404(Customer,pk=id)
    if req.method == 'GET':
        serializer = CustomerSerializer(customer)
        # print("serializer ", serializer.data)
        return Response(serializer.data)
    elif req.method == 'PATCH':
        serializer = CustomerSerializer(customer, data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif req.method == 'DElETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# * Class base view
class ProductList(APIView): 
    def get(self,req,id):
        customer = get_object_or_404(Customer,pk=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def put(self,req,id):
        serializer = ProductSerializer(self.product,data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,req,id):
        if self.product.orderitem_set.count()>0:
            return Response({'error':'Product cannot be deleted'})
        self.product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
