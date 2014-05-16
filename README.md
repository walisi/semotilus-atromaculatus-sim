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

2. Température de l'eau

La température du plan d'eau est basée sur le calcul d'une courbe sinusoïdale.
C'est peut-être un indicateur valable du coefficient de température général du
bassin d'eau à un moment de l'année, même si la température est très variable
d'un point à l'autre. La température réelle pourrait provenir d'un recensement,
si ces données étaient disponibles.

3. Exécution de la simulation

La simulation est exécutée hors-ligne, à partir d'une collection limitée de
données statiques, avec un résultat unique. L'utilisation d'une base de données
exhaustive nécessiterait un moteur de simulation plus performant. Une interface
améliorée pourrait permettre d'interroger le modèle en ligne, avec un résultat
graphique sous forme de classement.

4. Evolution de la répartition de la ressource

Le modèle de simulation est statique. Il ne réflète pas l'évolution de la
population de l'espèce d'une année à l'autre, à cause de différents facteurs :
population antérieure, restriction à l'exploitation, etc.
