from django.urls import path
from verification.views import VerifyEmailView    

urlpatterns = [
    path('verify/<str:token>/', VerifyEmailView.as_view(), name='verify-email'),
]
