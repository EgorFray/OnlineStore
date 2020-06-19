from django.urls import path, include
from . import views
from rest_framework import routers

games_router = routers.DefaultRouter()
games_router.register('goods', views.UltraGameView, basename='goods')
games_router.register('orders', views.OrdersView, basename='orders')
app_name = 'store'

urlpatterns = [
    path('', include(games_router.urls)),
]
