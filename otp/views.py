import random
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.utils import timezone

from authforge.accounts.models import User
from .models import OTP
    # Create your views here.

user = get_user_model()

class SendOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
        except user.DoesNotExist:
            return Response({"error": "User with this email does not exist."}, status=400)

        otp_code = str(random.randint(100000, 999999))
            
        OTP.objects.create(user=user, code=otp_code)

            # Here you would integrate with an email service to send the OTP to the user's email.
        print(f"OTP for {email}: {otp_code}")  # For demonstration purposes only

        return Response({"message": "OTP sent to email."}, status=200)
    


class VerifyOTPView(APIView):
    def post(self, request):
        email = request.data.get("email")
        code = request.data.get("code")

        user = User.objects.filter(email=email).first()
        if not user:
            return Response({"error": "User not found"}, status=404)

        otp = OTP.objects.filter(user=user, code=code).last()

        if not otp:
            return Response({"error": "Invalid OTP"}, status=400)

        if otp.is_expired():
            otp.delete()
            return Response({"error": "OTP expired"}, status=400)

        otp.delete()
        return Response({"msg": "OTP verified"})