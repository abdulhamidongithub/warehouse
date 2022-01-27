from django.db import models
from app1.models import Client, Ombor, Product

class Stats(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    sanasi = models.DateTimeField()
    miqdor = models.PositiveSmallIntegerField()
    umumiy_summa = models.IntegerField()
    tolandi = models.IntegerField()
    nasiya = models.IntegerField()
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.client.ism}, {self.product.nom} ({self.miqdor}), {self.sanasi} "

