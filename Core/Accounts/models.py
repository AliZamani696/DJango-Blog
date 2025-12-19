from enum import unique
from re import T
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db.models.fields.files import default_storage
from django.db.models.functions import Abs
from django.utils.translation import gettext_lazy as _
from django.utils import timezone, tree
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.






class CustomUserManager(BaseUserManager):
    def CreateUser(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError(_("email is required"))
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_active",True)
        extra_fields.setdefault("is_superuser",True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("superuser must have is_staff=True"))

        if extra_fields.get("is_active") is not True:
            raise ValueError(_("superuser must have is_active=True"))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("superuser must have is_superuser=True"))


        return self.CreateUser(email,password,**extra_fields)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        _("email"),
        unique=True,
        db_index = True
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False
    )
    is_active = models.BooleanField(
        _("active"),
        default=True
    )
    is_superuser = models.BooleanField(
        _("super user"),
        default=False
    )
    date_joined = models.DateTimeField(
        _("date joined"),
        default=timezone.now
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    profile_image = models.ImageField(
        upload_to = "profile_images/",
        null = True,
        blank = True,
    )
    bio = models.TextField(
        _("Bio"),
        blank = True
    )

    email_verified = models.BooleanField(
        default=False
    )


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    class Meta:
        ordering = ["-date_joined"]

    def __str__(self):
        return self.email
