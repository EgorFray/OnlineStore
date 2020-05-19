from django.urls import include, path
from django.conf.urls import url
from . import views
from django.urls import include, path
from rest_framework import routers

app_name = 'store'
router = routers.DefaultRouter()
router.register(r'allgames', views.GoodsViewSet, basename='allgames')
router.register(r'cart', views.CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
    path('allgames/',views.GoodsViewSet),
    path('cart/', views.CartViewSet),
]
