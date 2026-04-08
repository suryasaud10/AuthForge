from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from verification.models import EmailVerification

# Create your views here.

class VerifyEmailView(APIView):
    def get(self, request, token):
        record = EmailVerification.objects.filter(token=token).first()

        if not record:
            return Response({"error": "Invalid token"}, status=400)

        user = record.user
        user.is_verified = True
        user.save()
        
        record.delete()  # Optionally delete the verification record after successful verification
        return Response({"message": "Email verified successfully"}, status=200)


