from django.urls import path
# from rest_framework.authtoken import views
from .views import (
    CustomAuthToken, 
    LogoutAuthToken, 
    RegistrationAPIView,
    ForgotPasswordAPIView,
    VerifyPasswordAPIView,
    UpdatePasswordAPIView
)


urlpatterns = [
    path('auth/login', CustomAuthToken.as_view()),
    path('auth/logout', LogoutAuthToken.as_view()),
    path('auth/registration', RegistrationAPIView.as_view()),
    path('auth/password_forgot', ForgotPasswordAPIView.as_view()),
    path('auth/password_verify', VerifyPasswordAPIView.as_view()),
    path('auth/password_update', UpdatePasswordAPIView.as_view()),
]