from django.shortcuts import render
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     RetrieveUpdateAPIView,
                                     DestroyAPIView)

# Create your views here.
from .models import Goods, Orders
from .serializers import (GamesSerializer,
                          GameItemSerializer,
                          OrdersSerializer)
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.response import Response


# Get a list with all games
class GamesListView(ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GamesSerializer
    # serializer = GamesSerializer(queryset, context={'request':None})


# Get detail of one game
class GamesDetailView(RetrieveAPIView):
    queryset = Goods.objects.all()
    serializer_class = GameItemSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


# Update data of one game
class GamesUpdateView(RetrieveUpdateAPIView):
    queryset = Goods.objects.all()
    serializer_class = GameItemSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


# Delete data of one game
class GamesDeleteView(DestroyAPIView):
    queryset = Goods.objects.all()
    serializer_class = GameItemSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


# View for Orders
class OrdersView(RetrieveUpdateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    lookup_field = 'orders'
    lookup_url_kwarg = 'orders'

    def get_queryset(self):
        queryset = self.queryset.filter()
        return queryset

    def perform_create(self, serializer):
        serializer.save(self.request)







        






















