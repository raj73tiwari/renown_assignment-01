from django.urls import path
from .views import UserSignUp, UserLogin, UpdateFullName, GenerateOTP

urlpatterns = [
    path('signup/', UserSignUp.as_view(), name='signup'),
    path('login/', UserLogin.as_view(), name='login'),
    path('gen-otp/',GenerateOTP.as_view(), name='gen-otp'),
    path('update-fullname/', UpdateFullName.as_view(), name='update-fullname'),
]