from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("O campo email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    TIPO_CHOICES = (
        ('Guia', 'Guia'),
        ('Aventureiro', 'Aventureiro'),
    )
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255, null=True)
    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        default='Aventureiro'
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='userapi_usuario_set', 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='userapi_usuario_permissions',
        blank=True
    )

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nome']

    def __str__(self):
        return self.email