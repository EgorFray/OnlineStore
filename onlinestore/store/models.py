from django.db import models
from rest_framework.reverse import reverse
from django.utils.text import slugify


# Create your models here.
class Goods(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(max_length=5000, null=False, blank=False)
    price = models.CharField(max_length=20, null=False, blank=False)
    slug = models.SlugField(blank=True, unique=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Goods, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Orders(models.Model):
    DELIVERY_CHOICES = [
        ('Nova poshta', 'Nova poshta'),
        ('Ukrposhta', 'Ukrposhta'),
        ('Self PickUp', 'Self PickUp')
    ]
    PAYMENT_CHOICES = [
        ('Card', 'Card'),
        ('Cash', 'Cash')
    ]
    COUNTRY_CHOICES = [
        ('Ukraine', 'Ukraine'),
        ('Russia', 'Russia')
    ]
    order_name = models.CharField(max_length=20, default='Order name')
    date_created = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Goods, default='')
    delivery_method = models.CharField(max_length=30, choices=DELIVERY_CHOICES, default='')
    payment_method = models.CharField(max_length=30, choices=PAYMENT_CHOICES, default='')
    country = models.CharField(max_length=30, choices=COUNTRY_CHOICES, default='')
    city = models.CharField(max_length=30, default='')
    address = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.order_name




