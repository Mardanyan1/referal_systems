import random
import time

from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

from django.shortcuts import render, redirect


class UserRegistrationPhone(APIView):
    # def get(self, request):
    #     return Response({'message': 'Please enter your phone number'}, status=status.HTTP_200_OK)

    def post(self, request):
        if 'phone_number' in request.data:
            phone_number = request.data['phone_number']
            request.session['phone_number'] = phone_number
            time.sleep(2)
            return render(request, 'account/register_password.html')

        elif 'password' in request.data:
            phone_number = request.session.get('phone_number')
            if phone_number:
                password = request.data['password']
                invite_code = random.randint(100000, 999999)
                user = User.objects.create(phone_number=phone_number, password=make_password(password),
                                           invite_code=invite_code)
                user.save()
                del request.session['phone_number']
                serializer = UserSerializer(user)
                # return Response(serializer.data, status=status.HTTP_201_CREATED)
                return redirect('profile')
            else:
                return Response({'error': 'Номер телефона не найден в сессии.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Неверные данные запроса.'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return render(request, 'account/registration.html')


class UserAuthentication(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')
        try:
            user = User.objects.get(phone_number=phone_number)
            if check_password(password, user.password):
                # return Response({'message': 'Logged in successfully'}, status=status.HTTP_200_OK)
                return redirect('profile')

            return Response({'error': 'Invalid phone number or password'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({'error': 'Invalid phone number or password'}, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        return render(request, 'account/login.html')


class UserProfile(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        return render(request, 'account/profile.html', {'user': user})