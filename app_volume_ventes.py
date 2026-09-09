import pandas as pd
import plotly.express as px

# Chargement des ventes
ventes = pd.read_csv('ventes.csv')

# Addition des quantités vendues pour chaque produit
ventes_produit = ventes.groupby('produit', as_index=False)['qte'].sum()
ventes_produit = ventes_produit.rename(columns={'qte': 'quantite_vendue'})

# Création du graphique des ventes par produit
figure = px.bar(
    ventes_produit,
    x='produit',
    y='quantite_vendue',
    title='Ventes par produit',
    labels={'produit': 'Produit', 'quantite_vendue': 'Quantité vendue'},
    text_auto=True
)
figure.write_html('ventes-par-produit.html')

print('ventes-par-produit.html généré avec succès !')