from django.shortcuts import render
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     RetrieveUpdateAPIView,
                                     DestroyAPIView,
                                     CreateAPIView,
                                     )

# Create your views here.
from .models import Goods, Orders, OrdersDetail
from .serializers import (GamesSerializer,
                          GameItemSerializer,
                          OrdersSerializer,
                          OrdersDetailSerializer,
                          GameCreateSerializer)
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.response import Response


# Get a list with all games
class GamesListView(ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GamesSerializer
    lookup_field = 'slug'


class GameCreateApiView(CreateAPIView):
    queryset = Goods.objects.all()
    serializer_class = GameCreateSerializer


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
class OrdersView(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def get_queryset(self):
        queryset = self.queryset.filter()
        return queryset

    def perform_create(self, serializer):
        serializer.save()


class OrdersDetailView(viewsets.ModelViewSet):
    queryset = OrdersDetail.objects.all()
    serializer_class = OrdersDetailSerializer

    def perform_create(self, serializer):
        serializer.save()






        






















