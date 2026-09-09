import csv

# Dictionnaire des quantités vendues par produit
total_ventes_produit = {}

# Lecture du fichier CSV sans utiliser Pandas
with open('ventes.csv', newline='', encoding='utf-8') as fichier:
    ventes = csv.DictReader(fichier)

    # Pour chaque vente, on récupère le produit et sa quantité
    for vente in ventes:
        produit = vente['produit']
        quantite = int(vente['qte'])

        # On additionne les quantités pour un même produit
        if produit in total_ventes_produit:
            total_ventes_produit[produit] += quantite
        else:
            total_ventes_produit[produit] = quantite

# Recherche du produit le plus vendu et du produit le moins vendu
produit_plus_vendu = max(total_ventes_produit, key=total_ventes_produit.get)
produit_moins_vendu = min(total_ventes_produit, key=total_ventes_produit.get)

print(f'Le produit le plus vendu est {produit_plus_vendu} avec {total_ventes_produit[produit_plus_vendu]} unités.')
print(f'Le produit le moins vendu est {produit_moins_vendu} avec {total_ventes_produit[produit_moins_vendu]} unités.')