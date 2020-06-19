from rest_framework import serializers

from .models import Goods, Orders


class GameItemSerializer(serializers. ModelSerializer):
    class Meta:
        model = Goods
        fields = ['title', 'body', 'price']


class GameCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['title', 'body', 'price']


class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['id', 'title', 'body', 'price', 'slug']


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['order_name', 'items', 'delivery_method', 'payment_method', 'country', 'city', 'address']

