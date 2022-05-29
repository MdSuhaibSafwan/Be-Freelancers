from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.translation import gettext_lazy as _
from base_lib.model import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
                    )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    full_name = models.CharField(_("Full Name"),max_length=100)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)

    date_created = models.DateTimeField(_("Date User Created"), auto_now_add=True)
    last_updated = models.DateTimeField(_("Date Last Updated"), auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return f"Email: {self.email}"
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.staff

    @property
    def is_superuser(self):
        "Is the user a superuser?"
        return self.superuser


class Client(BaseModel):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False)
    username = models.CharField(_("Username"), max_length=20, editable=False, unique=True)
    client_type = models.CharField(max_length=100)
    description = models.TextField(_("DESCRIBE YOURSELF"))
    country = models.CharField(max_length=50)

    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Developer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False)
    username = models.CharField(_("Username"), max_length=20, editable=False, unique=True)
    client_type = models.CharField(max_length=100)
    description = models.TextField(_("DESCRIBE YOURSELF"))
    country = models.CharField(max_length=50)

    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
