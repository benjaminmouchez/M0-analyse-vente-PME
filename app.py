import plotly.express as px
import pandas as pd

# Chargement des données
ventes = pd.read_csv('ventes.csv')

# Création du graphique des quantités vendues par région
figure = px.pie(ventes, values='qte', names='region', title='quantité vendue par région')
figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')
