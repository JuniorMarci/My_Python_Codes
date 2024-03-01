from django.db import models

# Create your models here.
class Tab(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.hashers import make_password

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O e-mail deve ser fornecido.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    nome = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


from django.db import models

class Chamada(models.Model):
    inicio_chamada = models.DateTimeField()
    duracao = models.DurationField()
    agentes = models.ManyToManyField('Agente', related_name='chamadas')
    interlocutores = models.ManyToManyField('Interlocutor', related_name='chamadas')
    servico = models.CharField(max_length=100)
    habilidades = models.CharField(max_length=100)
    id_chamada = models.CharField(max_length=100)
    arquivo = models.CharField(max_length=100)

class Agente(models.Model):
    nome = models.CharField(max_length=100)

class Interlocutor(models.Model):
    nome = models.CharField(max_length=100)
