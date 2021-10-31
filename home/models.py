from django.db import models

# Create your models here.
class Diario(models.Model):
    fecasi = models.DateField(blank=True,null=True)
    lib = models.CharField(max_length=20,null=True,blank=True)
    nroasi = models.IntegerField(blank=False,null=False)
    nrodoc = models.CharField(max_length=20,null=True,blank=True)
    codcta = models.CharField(max_length=20,null=True,blank=True)
    monmn = models.FloatField(blank=False,null=False)


