from django.db import models
from django.utils.text import slugify


# Create your models here.
class Goods(models.Model):
    class Meta:
        ordering = ['id']

    CURRENCY_CHOICES = [
        ('UAH', 'UAH')
    ]
    title = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(max_length=5000, null=False, blank=False)
    price = models.IntegerField(unique=False)
    currency = models.CharField(max_length=10, null=True, choices=CURRENCY_CHOICES)
    slug = models.SlugField(blank=True, unique=True)

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
    date_created = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Goods)
    delivery_method = models.CharField(max_length=30, choices=DELIVERY_CHOICES)
    payment_method = models.CharField(max_length=30, choices=PAYMENT_CHOICES)
    country = models.CharField(max_length=30, choices=COUNTRY_CHOICES)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=60)







