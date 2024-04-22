from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.UserAPIView.as_view(), name='login'),
    path('registration/', views.UserRegistrationAPIView.as_view(), name='registration'),
    path('profile/', views.UserRegistrationAPIView.as_view(), name='profile'),

]
