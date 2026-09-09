import pandas as pd

# Chargement du jeu de données
ventes = pd.read_csv('ventes.csv')

# Calcul du chiffre d'affaires pour chaque ligne
ventes['chiffre_affaires'] = ventes['prix'] * ventes['qte']

# Calcul des indicateurs demandés pour chaque produit
statistiques_produits = ventes.groupby('produit').agg(
    chiffre_affaires_moyen=('chiffre_affaires', 'mean'),
    chiffre_affaires_median=('chiffre_affaires', 'median'),
    volume_ventes_moyen=('qte', 'mean'),
    volume_ventes_median=('qte', 'median'),
    volume_ventes_ecart_type=('qte', 'std'),
    volume_ventes_variance=('qte', 'var')
).reset_index()

print(statistiques_produits.to_string(index=False))