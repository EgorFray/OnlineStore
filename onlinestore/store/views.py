
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from .models import Goods, Orders
from .serializers import (GamesSerializer,
                          GameItemSerializer,
                          OrdersSerializer,
                          GameCreateSerializer)
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class UltraGameView(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def list(self, request):
        queryset = Goods.objects.all()
        serializer = GameItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        queryset = Goods.objects.create()
        serializer = GameCreateSerializer(queryset, data= request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, slug=None):
        queryset = Goods.objects.get(slug=slug)
        serializer = GamesSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, slug=None):
        queryset = Goods.objects.get(slug=slug)
        serializer = GamesSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def destroy(self, request, slug=None):
        queryset = Goods.objects.get(slug=slug)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# View for Orders
class OrdersView(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [AllowAny]

#    def post(self, request, *args, **kwargs):
#        serializer = OrdersSerializer(data=request.data)
#        if serializer.is_valid():
#            order = serializer.save()
#            serializer = OrdersSerializer(order)
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)











        






















