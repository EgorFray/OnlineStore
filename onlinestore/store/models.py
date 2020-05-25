from django.db import models
from rest_framework.reverse import reverse

# Create your models here.
class Goods(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(max_length=5000, null=False, blank=False)
    price = models.CharField(max_length=20, null=False, blank=False)
    slug = models.SlugField(blank=True, unique=False)

    def __str__(self):
        return self.title


class Orders(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Goods)
    delivery_method = models.CharField(max_length=30, default='')
    payment_method = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.items

