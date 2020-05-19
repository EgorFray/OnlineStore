from rest_framework import serializers

from .models import Goods, Cart


class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['id', 'title', 'body', 'price', 'slug']


class GameItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['title', 'body', 'price', 'slug']


class CartSerializer(serializers.ModelSerializer):
    items = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='cart-detail'
    )
    class Meta:
        model = Cart
        fields = ['items']