from rest_framework import generics
from .serializers import CustomLoginSerializer, RegisterSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView  

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer  


class ProfileView(APIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({
            'email': request.user.email,
            'name': request.user.name
        })
    

class LoginView(TokenObtainPairView):
    serializer_class = CustomLoginSerializer