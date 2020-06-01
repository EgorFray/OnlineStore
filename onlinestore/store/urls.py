from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('orders', views.OrdersView, basename='orders-detail')
router.register('orders-list', views.OrdersDetailView, basename='orders-list-detail')


app_name = 'store'

urlpatterns = [
    path('cart/', include(router.urls)),
    url(r'^create', views.GameCreateApiView.as_view(), name='create'),
    url(r'^$', views.GamesListView.as_view(), name='games-list'),
    url(r'^(?P<slug>[\w-]+)/$', views.GamesDetailView.as_view(), name='games-detail'),
    url(r'^(?P<slug>[\w-]+)/update', views.GamesUpdateView.as_view(), name='games-update'),
    url(r'^(?P<slug>[\w-]+)/delete', views.GamesDeleteView.as_view(), name='games-delete'),
]
