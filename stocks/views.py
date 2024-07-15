# views.py
from rest_framework import viewsets
from .models import Stock
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer, RegisterSerializer,StockSerializer,ChangePasswordSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class LogoutView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=204)
        except Exception as e:
            return Response(status=400)
class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            new_password = serializer.data.get("new_password")
            user = authenticate(username=request.user.username, password=old_password)
            if user:
                user.set_password(new_password)
                user.save()
                return Response({"status": "password set"}, status=status.HTTP_200_OK)
            else:
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        