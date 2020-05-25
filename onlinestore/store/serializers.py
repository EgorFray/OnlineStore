from rest_framework import serializers

from .models import Goods, Orders


class GamesSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='games-item',
        lookup_field='slug',
        read_only=True
    )
    class Meta:
        model = Goods
        fields = ['id', 'url', 'title', 'body', 'price', 'slug']


class GameItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goods
        fields = ['title', 'url', 'body', 'price', 'slug']


class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        fields = ['url', 'items', 'delivery_method', 'payment_method']
