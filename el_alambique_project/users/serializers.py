from rest_framework import serializers
from .models import CustomUser
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

class UserRegisterSerializer(serializers.ModelSerializer):
    password_check = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password_check')
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}},
            'first_name': {'required': False},
            'last_name': {'required': False},
        }

    def validate(self, data):
        if data['password'] != data['password_check']:
            raise serializers.ValidationError("Паролі не співпадають!")


        user_data = data.copy()
        user_data.pop('password_check')

        try:
            validate_password(data['password'], user=CustomUser(**user_data))
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)

        return data

    def create(self, validated_data):
        validated_data.pop('password_check')
        user = CustomUser.objects.create_user(**validated_data)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        read_only_fields = ('email',)
        