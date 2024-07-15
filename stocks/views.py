# views.py
from rest_framework import viewsets
from .models import Stock
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer, RegisterSerializer,StockSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password, make_password
import json
from .models import UserPassword

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        password = data.get('password')
        user_password = UserPassword.objects.first()
        if user_password:
            # Check if the stored password is hashed
            if user_password.password.startswith('pbkdf2_'):
                if check_password(password, user_password.password):
                    return JsonResponse({'message': 'Login successful'}, status=200)
            else:
                # If the password is not hashed, compare directly and update it to a hashed version
                if user_password.password == password:
                    user_password.password = make_password(password)
                    user_password.save()
                    return JsonResponse({'message': 'Login successful'}, status=200)
        return JsonResponse({'message': 'Invalid password'}, status=401)

@csrf_exempt
def change_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        old_password = data.get('old_password')
        new_password = data.get('new_password')
        user_password = UserPassword.objects.first()
        if user_password:
            # Check if the stored password is hashed
            if user_password.password.startswith('pbkdf2_'):
                if check_password(old_password, user_password.password):
                    user_password.password = make_password(new_password)
                    user_password.save()
                    return JsonResponse({'message': 'Password changed successfully'}, status=200)
            else:
                # If the password is not hashed, compare directly and update it to a hashed version
                if user_password.password == old_password:
                    user_password.password = make_password(new_password)
                    user_password.save()
                    return JsonResponse({'message': 'Password changed successfully'}, status=200)
        return JsonResponse({'message': 'Invalid old password'}, status=401)