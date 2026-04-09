from rest_framework.views import APIView
from rest_framework.response import Response
from verification.models import EmailVerification
from django.shortcuts import get_object_or_404

# Create your views here.

class VerifyEmailView(APIView):
    def get(self, request, token):
        record = get_object_or_404(EmailVerification, token=token)

        if record.user.is_verified:
            return Response({"message": "Email is already verified"}, status=200)
        
        user = record.user
        user.is_verified = True
        user.save(update_fields=['is_verified'])
        
        record.delete()  # Optionally delete the verification record after successful verification
        
        return Response({"message": "Email verified successfully"}, status=200)


