from django.db import models

# Create your models here.
class Collecte(models.Model):
    id = models.IntegerField(primary_key=True)
    sweater= models.IntegerField()
    underwear = models.IntegerField()
    pant = models.IntegerField()
    jacket = models.IntegerField()

class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    nbr_enfant = models.IntegerField()
    metier = models.CharField(max_length=100)
    prix_total= models.IntegerField()
    collect_data = models.OneToOneField(Collecte, on_delete=models.CASCADE, null=True)