from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException

from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist

from .serializers import (
    CustomAuthTokenSerializer, 
    RegistrationSerializer, 
    ForgotPasswordSerializer,
    VerifyPasswordSerializer,
    UpdatePasswordSerializer
)
from .models import User


class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "contry": user.contry,
            "city": user.city
        }, status=200)


class LogoutAuthToken(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request, *args, **kwargs):
        user = request.user
        token = Token.objects.get(user=user)
        token.delete()
        return Response(status=204)
    

class CustomAPIView(APIView):
    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)
    

class RegistrationAPIView(CustomAPIView):
    # Регистрация
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    

class ForgotPasswordAPIView(CustomAPIView):
    """Отправить письмо на почту с кодом"""
    serializer_class = ForgotPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email=serializer.data["email"]
        user = get_object_or_404(User, email=email)
        user.update() # создать код для восстановления
        # user.update({"otp": make_random_otp()})
        # send email with otp
        send_mail(
            subject=f'Привет! {email}',
            message=f'Код для восстановления пароля: {user.otp}',
            from_email='noreply@church.com',
            recipient_list=[email,]
        )
        succes = {'detail': 'Код для восстановления пароля отправлен на Ваш email'}
        return Response(succes, status=201)


class VerifyPasswordAPIView(CustomAPIView):
    """Подтвердить код из письма"""
    serializer_class = VerifyPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data["email"]
        otp = serializer.data["otp_code"]
        try:
            user = User.objects.get(email=email, otp=otp)
        except ObjectDoesNotExist:
            raise APIException(code=400, detail="Неверный код из письма")
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        }, status=200)


class UpdatePasswordAPIView(CustomAPIView):
    """Подтвердить код из письма"""
    permission_classes = [IsAuthenticated,]
    serializer_class = UpdatePasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.data["new_password"]
        user = request.user
        user.set_password(password)
        user.save()
        return Response({"detail": "Пароль успешно изменён"}, status=200)
