from django.shortcuts import render

# Create your views here.
import requests
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Goods
from .serializers import GamesSerializer
from django.shortcuts import get_object_or_404


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GamesSerializer

    def create(self, request):
        serializer = GamesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Goods.objects.all()
        game = get_object_or_404(queryset, pk=pk)
        serializer = GamesSerializer(game)
        return Response(serializer.data)

    def update(self, request, pk=None):
        game = Goods.objects.get(pk=pk)
        serializer = GamesSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)












