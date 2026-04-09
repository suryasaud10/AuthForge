from django.urls import path
from .views import SendOTPView, VerifyOTPView

urlpatterns = [
    path('send/', SendOTPView.as_view()),
    path('verify/', VerifyOTPView.as_view()),
]