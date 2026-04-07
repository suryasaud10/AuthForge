from rest_framework import generics
from .serializers import RegisterSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

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