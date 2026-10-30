-- a. Chiffre d'affaires total
SELECT SUM(ventes.c3 * ventes.c4) AS chiffre_affaires_total
FROM ventes;

-- b. Ventes par produit
SELECT
    ventes.c2 AS produit,
    SUM(ventes.c4) AS quantite_vendue,
    SUM(ventes.c3 * ventes.c4) AS chiffre_affaires
FROM ventes
GROUP BY ventes.c2
ORDER BY chiffre_affaires DESC;

-- c. Ventes par région
SELECT
    ventes.c5 AS region,
    SUM(ventes.c4) AS quantite_vendue,
    SUM(ventes.c3 * ventes.c4) AS chiffre_affaires
FROM ventes
GROUP BY ventes.c5
ORDER BY chiffre_affaires DESC;

