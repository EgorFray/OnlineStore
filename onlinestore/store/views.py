from django.shortcuts import render

# Create your views here.
import requests
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Goods
from .serializers import GamesSerializer


class GoodsViewSet(viewsets.ModelViewSet):
    def api_detail_store_view(self, request, slug):
        try:
            product = Goods.objects.get(slug=slug)
        except Goods.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def detection_of_method(self, request, slug):
        if request.method == "GET":
            serializer = GamesSerializer(Goods)
            return Response(serializer.data)

    def product_list(self):
        products = Goods.objects.all()
        return products





