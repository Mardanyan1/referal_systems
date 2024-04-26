import random
import time

from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

from django.shortcuts import render, redirect


class UserRegistrationPhone(APIView):
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
                # return render(request, 'account/profile.html', {'user_data': serializer.data})

            else:
                return Response({'error': 'Номер телефона не найден в сессии.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Неверные данные запроса.'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return render(request, 'account/registration.html')


class UserAuthentication(APIView):
    def post(self, request):
        if 'phone_number' in request.data and 'password' in request.data:
            phone_number = request.data.get('phone_number')
            request.session['phone_number'] = phone_number

            password = request.data.get('password')
            try:
                user = User.objects.get(phone_number=phone_number)
                if check_password(password, user.password):
                    serializer = UserSerializer(user)

                    # return Response(serializer.data, status=status.HTTP_200_OK)
                    return render(request, 'account/profile.html', {'user_data': serializer.data})
            except User.DoesNotExist:
                return Response({'error': 'Неверный логин или пароль'}, status=status.HTTP_401_UNAUTHORIZEDy)
        elif 'invited_by' in request.data:
            invited_by = request.data.get('invited_by')
            if invited_by:
                invited_user = User.objects.get(invite_code=invited_by)

                phone_number = request.session.get('phone_number')
                user = User.objects.get(phone_number=phone_number)
                if invited_user and (user.invite_code != invited_by):
                    invited_users = User.objects.filter(invited_by=user.invite_code)

                    del request.session['phone_number']

                    user.invited_by = invited_by
                    user.save()
                    serializer = UserSerializer(user)
                    return render(request, 'account/profile.html', {'user_data': serializer.data, 'invited_users':invited_users})
                    # return Response({'message': 'Invite code activated successfully'}, status=201)
                else:
                    return Response({'error': 'Пользователь не может пригласить самого себя'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'error': 'Введите инвайт-код'}, status=400)

    def get(self, request):
        return render(request, 'account/login.html')
