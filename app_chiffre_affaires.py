import pandas as pd
import plotly.express as px

# Chargement du fichier de ventes
ventes = pd.read_csv('ventes.csv')

# Calcul du chiffre d'affaires de chaque vente
ventes['chiffre_affaires'] = ventes['prix'] * ventes['qte']

# Total du chiffre d'affaires pour chaque produit
chiffre_affaires_produit = ventes.groupby('produit', as_index=False)['chiffre_affaires'].sum()

# Création du graphique du chiffre d'affaires par produit
figure = px.bar(
    chiffre_affaires_produit,
    x='produit',
    y='chiffre_affaires',
    title="Chiffre d'affaires par produit",
    labels={'produit': 'Produit', 'chiffre_affaires': "Chiffre d'affaires (€)"},
    text_auto=True
)
figure.write_html('chiffre-affaires-par-produit.html')

print('chiffre-affaires-par-produit.html généré avec succès !')