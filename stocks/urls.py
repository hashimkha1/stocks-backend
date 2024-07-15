# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StockViewSet,login,change_password

router = DefaultRouter()
router.register(r'stocks', StockViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
     path('api/login/', login),
    path('api/change-password/', change_password)
]
