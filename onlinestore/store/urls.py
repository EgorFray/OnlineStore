from django.urls import include, path
from django.conf.urls import url
from . import views

app_name = 'store'

urlpatterns = [
    # url(r'orders', views.OrdersView.as_view(), name='orders'),
    url(r'^$', views.GamesListView.as_view(), name='games-list'),
    url(r'^(?P<slug>[\w-]+)/$', views.GamesDetailView.as_view(), name='games-item'),
    url(r'^(?P<slug>[\w-]+)/update', views.GamesUpdateView.as_view(), name='games-update'),
    url(r'^(?P<slug>[\w-]+)/delete', views.GamesDeleteView.as_view(), name='games-delete'),
]