import random
from django.utils import timezone
import csv
from models import Client, Collecte
from métier import metier


# Données pour le modèle Client :
for i in range(1000):
    Client.objects.create(
        id=i+1,
        nbr_enfant=random.randint(0, 5),
        metier=random.choice(metier),
        prix_total=random.randint(0,1),
    )

# Données pour le modèle CollectData :
for i in range(1000):
    Collecte.objects.create(
        id=i+1,
        sweater = random.randint(20, 75),
        pant = random.randint(25, 150),
        underwear = random.randint(5, 20),
        jacket = random.randint(50, 300),
    )

    # Calculer le montant total dépensé pour cette transaction
    prix_total = sweater + underwear + pant + jacket
    Client.objects.update(
        prix_total=prix_total,
    )


# Exporter les données pour le modèle Client
with open('Data_client.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'nbr_enfant', 'metier', 'prix_total'])

    for client in Client.objects.all():
        writer.writerow([client.id, client.nbr_enfant ,client.metier, client.prix_total])

# Exporter les données pour le modèle CollectData
with open('Data_collecte.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'sweater', 'underwear', 'pant', 'jacket'])

    for collecte in Collecte.objects.all():
        writer.writerow([collecte.id, collecte.sweater, collecte.underwear, collecte.pant, collecte.jacket])
