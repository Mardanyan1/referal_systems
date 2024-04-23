from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegistrationPhone.as_view(), name='registration_page'),
    path('login/', UserAuthentication.as_view(), name='login_page'),
    path('register/password/', UserRegistrationPhone.as_view(), name='register_password'),
    path('profile/', UserProfile.as_view(), name='profile'),

]
