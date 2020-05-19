from django.shortcuts import render

# Create your views here.
from .models import Goods, Cart
from rest_framework import viewsets
from .serializers import GamesSerializer, CartSerializer, GameItemSerializer
from django.http import HttpResponse, JsonResponse


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GamesSerializer


class ItemDetailViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GameItemSerializer
    lookup_field = 'slug'


class CartViewSet(viewsets.ModelViewSet):
    model = Cart
    serializer_class = CartSerializer
    lookup_field = 'cart'

    def get_queryset(self):
        return Cart.objects.all()

    def add(self, request, pk):
        return JsonResponse({'success':True})

    def pre_save(self, obj):
        obj = self.request







        






















