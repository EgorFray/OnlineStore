from rest_framework import serializers

from .models import Goods, Orders, OrdersDetail


class GameItemSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api-store:games-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Goods
        fields = ['url', 'title', 'body', 'price', 'slug']


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
        fields = ['order_name', 'items', 'delivery_method', 'payment_method']


class OrdersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdersDetail
        fields = ['order_name', 'country', 'city', 'address']