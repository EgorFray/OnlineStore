from django.contrib import admin
from .models import Goods, Orders, OrdersDetail


# Register your models here.

admin.site.register(Goods)
admin.site.register(Orders)
admin.site.register(OrdersDetail)