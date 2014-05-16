semotilus-atromaculatus-sim
===========================

Semotilus Atromaculatus Sim est l'épreuve 3 du concours de programmation.

1. Utilisation

1.1 Test

Lancer la routine de validation du programme avec la commande suivante.

python -m unittest test_simulation

1.2 Usage

Lancer la simulation avec la commande suivante. La simulation accepte un
paramètre contenant la date. Le résultat affiché est le nom du meilleur plan
d'eau pour la date donnée. La date d'aujourd'hui est utilisée si aucune date
n'est donnée. La date est composée du mois suivi d'un tiret et du jour.

python semotilus_atromaculatus_simulator.py 07-15

Discussion
==========

1. Emplacement des lieux de pêche

Certains plans d'eau peuvent couvrir une grande étendue où la répartition de
la ressource est variable. Ces plans d'eau devrait être divisés en secteurs.
