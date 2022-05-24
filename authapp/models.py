from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


class CustomUserManager(BaseUserManager):
    def create_user(
        self, email, username, password, first_name, last_name, **other_fields
    ):
        if not email:
            raise ValueError(_("Pls provide email"))
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self, email, username, password, first_name, last_name, **other_fields
    ):

        # other_fields.setdefault('is_active', True)
        user = self.create_user(email, username, password, first_name, last_name)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Email address"), unique=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    country = CountryField(blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["pk"]
