# Create your models here.
from django.db import models
from django.contrib.auth.models import User,BaseUserManager,AbstractUser
# Create your models here.


class MyUserManager(BaseUserManager):
    def _create_user(self, email, last_name,first_name, password=None, **extra_fields):
        """
        Creates and saves a User with the given email,first_name,
        last_name and password.
        """
        if not email:
            raise ValueError('L\'utlisateur doit avoir un adresse mail')

        user = self.model(
            email=self.normalize_email(email),
            last_name= last_name,
            first_name=first_name,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, last_name,first_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,last_name,first_name, password, **extra_fields)

    def create_superuser(self, email,last_name,first_name, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, first_name,
        last_name and password.
        """
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email,last_name,first_name, password, **extra_fields)

class MyUser(AbstractUser):
    username=None
    email = models.EmailField(
        verbose_name='Adresse Mail',
        max_length=255,
        unique=True,
    )
    last_name = models.CharField(verbose_name='Nom',max_length=100)
    first_name = models.CharField(verbose_name='Prenom',max_length=100)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name','first_name']

    def __str__(self):
        return self.last_name+' '+self.first_name
