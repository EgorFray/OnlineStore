from rest_framework import serializers

from .models import Goods, Orders

class GameItemSerializer(serializers. ModelSerializer):
    class Meta:
        model = Goods
        fields = ['title', 'body', 'price', 'slug']


class GameCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['title', 'body', 'price']


class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['id', 'title', 'body', 'price', 'slug']


class OrdersSerializer(serializers.ModelSerializer):
    items = GameItemSerializer(many=True)

    class Meta:
        model = Orders
        fields = '__all__'

    def create(self, validated_data):
        game_list = []
        items = validated_data.pop('items')
        order = Orders.objects.create(**validated_data)
        for item in items:
            game = Goods.objects.create(**item, orders=order)
            game_list.append(game)
        order.items.add(*game_list)
        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        orders = (instance.items).all()
        orders = list(orders)
        instance.delivery_method = validated_data.get('delivery_method', instance.delivery_method)
        instance.payment_method = validated_data.get('payment_method', instance.payment_method)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.country)
        instance.address = validated_data.get('address', instance.country)
        instance.save()

        for item_data in items_data:
            item = orders.pop(0)
            item.title = item_data.get('title', item.title)
            item.body = item_data.get('body', item.body)
            item.price = item_data.get('price', item.price)
            item.save()
        return instance











