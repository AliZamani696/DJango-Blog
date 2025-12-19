

from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate, user_login_failed
from django.utils.translation import gettext_lazy as  _
from .models import CustomUser




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'bio',
            'profile_image',
            'date_joined'
        ]

        read_only_fields = ['id','date_joined']
        extra_kwargs = {
            'email': {'required': True, 'allow_blank': False}
        }



class UserDetailSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
         fields = UserSerializer.Meta.fields + [
            'is_active',
            'email_verified',
            'updated_at'
        ]
         read_only_fields = UserSerializer.Meta.read_only_fields + [
             'is_active',
             'email_verified',
             'updated_at'
         ]



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        min_length=8,
        max_length=128,
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
    )
    class Meta:
        model = CustomUser
        fields =[
            'email',
            'password',
            'password2'
        ]
    def validate(self,attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password":_("didnt match")}
            )
        return attrs


    def create(self,validate_data):
        validate_data.pop("password2")
        user  = CustomUser.objects.CreateUser(**validate_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required = True
    )
    password = serializers.CharField(
        write_only = True,
        required = True,
        style = {'input_type':'password'},
    )
    def validate(self, attrs):
        email = attrs.get("emial")
        password = attrs.get("password")

        if email and password:
            user = authenticate(
                request= self.context.get("request"),
                email  = email,
                password = password
            )
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
            if not user.is_active:
                msg = _('User account is disabled.')
                raise serializers.ValidationError(msg, code='authorization')
            else:
                msg = _('Must include "email" and "password".')
                raise serializers.ValidationError(msg, code='authorization')
            attrs["user"] = user
            return user
