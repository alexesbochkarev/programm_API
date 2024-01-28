from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework.authtoken.models import Token
from rest_framework import serializers

from .models import User


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
    

class RegistrationSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    detail = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ('email', 'password',  'first_name', 'last_name', 'contry', 'city', 'status', 'detail')
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'write_only': True},
            'last_name': {'write_only': True},
            'contry': {'write_only': True},
            'token': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class VerifyPasswordSerializer(ForgotPasswordSerializer):
    otp_code = serializers.CharField()


class UpdatePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField()