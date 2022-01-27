from django.contrib.auth.models import User
from django.db import models

class Ombor(models.Model):
    ism = models.CharField(max_length=30)
    dokon_nomi = models.CharField(max_length=30)
    joylashuv = models.CharField(max_length=30)
    turi = models.CharField(max_length=30, blank=True)
    tel = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.ism} ({self.dokon_nomi})"

class Product(models.Model):
    nom = models.CharField(max_length=30)
    brend_nomi = models.CharField(max_length=30, blank=True)
    kelgan_narxi = models.IntegerField()
    sotuvdagi_narx = models.IntegerField()
    miqdor = models.IntegerField()
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.nom} ({self.brend_nomi})"

class Client(models.Model):
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    dokon_nomi = models.CharField(max_length=30)
    joylashuv = models.CharField(max_length=30)
    qarz = models.IntegerField(default=0)
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.ism} ({self.dokon_nomi})"

