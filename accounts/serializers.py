from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import uuid
from verification.models import EmailVerification

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user =  User.objects.create_user(**validated_data)

        token = str(uuid.uuid4())
        EmailVerification.objects.create(user=user, token=token)
        
        print(f"VERIFY URL: http://127.0.0.1:8000/api/verification/verify/{token}/")
        return user

class CustomLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        if not self.user.is_verified:
            raise serializers.ValidationError('Email is not verified.')
        
        return data
    
