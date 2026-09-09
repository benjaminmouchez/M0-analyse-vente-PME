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

for _, produit in statistiques_produits.iterrows():
    print(f"\n{produit['produit']}")
    print(f"  Chiffre d'affaires moyen : {produit['chiffre_affaires_moyen']:.2f} €")
    print(f"  Chiffre d'affaires médian : {produit['chiffre_affaires_median']:.2f} €")
    print(f"  Volume des ventes moyen : {produit['volume_ventes_moyen']:.2f} unités")
    print(f"  Volume des ventes médian : {produit['volume_ventes_median']:.2f} unités")
    print(f"  Écart-type du volume des ventes : {produit['volume_ventes_ecart_type']:.2f}")
    print(f"  Variance du volume des ventes : {produit['volume_ventes_variance']:.2f}")