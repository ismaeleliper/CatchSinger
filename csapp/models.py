from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


class InfoSobreUsuario(models.Model):

    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Categorias(models.Model):

    musica = models.BooleanField(default=False)
    palestras = models.BooleanField(default=False)
    humor = models.BooleanField(default=False)


