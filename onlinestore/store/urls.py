from django.urls import include, path
from . import views
from rest_framework import routers

app_name = 'store'
router = routers.DefaultRouter()
router.register(r'allgames', views.GoodsViewSet, basename='allgames')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
