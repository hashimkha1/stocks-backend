# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StockViewSet,RegisterView, LogoutView, ChangePasswordView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'stocks', StockViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change_password'),
]
