import random

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import RegistrationForm
from .models import *
from .serializers import *


class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            auth_code = serializer.validated_data['auth_code']
            invite_code = random.randint(100000, 999999)

            # Создаем пользователя
            user = User.objects.create_user(phone_number=phone_number, auth_code=auth_code, invite_code=invite_code)
            login(request, user)

            return redirect('profile')
            # return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        form = RegistrationForm()
        return render(request, 'account/regist.html', {'form': form})


class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            password = serializer.validated_data['password']

            # Аутентификация пользователя
            user = authenticate(request, phone_number=phone_number, password=password)
            if user is not None:
                login(request, user)
                return Response({'message': 'User logged in successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid phone number or password'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
