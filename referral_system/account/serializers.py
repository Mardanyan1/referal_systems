from rest_framework import serializers
from .models import User, UserProfile, InviteCodeRelation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class InviteCodeRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InviteCodeRelation
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    auth_code = serializers.CharField()