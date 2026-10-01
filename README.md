# Réflexe Turtle — EVA

Entraîneur de réflexe pour la décision de *turtle* sur le jeu EVA.

**→ https://mouflon23.github.io/EVA-turtle/**

Sur une carte à 3 points de capture, la turtle consiste à n'en garder qu'un seul.
L'adversaire en tient alors 2 et marque deux fois plus vite : la manœuvre ne tient
que si son reste à parcourir est plus grand que deux fois le nôtre.

Avec les scores affichés (maximum 100), ça se ramène à :

```
turtle possible  ⟺  nous × 2 − 100 > eux
```

Strictement supérieur : à égalité pile, c'est non. Notre score doit valoir au
moins 51, sinon la turtle est impossible même si l'adversaire est à 0.

Routine mentale conseillée : **retrancher 50, puis doubler** — `87 → 37 → 74`.
Identique à « doubler puis retrancher 100 », mais on ne dépasse jamais 50 avant
de doubler, ce qui rend les scores à l'unité près tenables de tête.

## Ce que l'outil mesure

- le temps de décision, chrono démarré après l'affichage réel du score, avec un
  délai aléatoire avant chaque carte pour empêcher d'anticiper au rythme ;
- la justesse, par tranche de marge — plus la marge est fine, plus la décision
  est difficile ;
- les **inversions** : à chaque erreur, la règle est recalculée avec les deux
  scores échangés, ce qui distingue une faute de lecture des camps d'une faute
  de calcul.

L'historique est conservé dans le stockage local du navigateur. Rien n'est
envoyé nulle part, il n'y a ni compte ni serveur.

## Développement

`index.html` est généré, ne pas l'éditer directement. La source est le fragment
publié comme Artifact Claude ; `build.py` l'enveloppe dans un document HTML
autonome (doctype, `<head>`, encodage, favicon) :

```
python3 build.py ../eva-turtle.html index.html
```
