from rest_framework import serializers

from .models import Goods


class GamesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goods
        fields = ['id','title', 'body', 'price']