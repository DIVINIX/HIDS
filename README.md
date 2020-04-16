# HIDS

Un HIDS ou Système de détection d’intrusion en français, permet de détecter des activités anormales comme des intrusions sur la cible analysée.  Un HIDS se comporte comme un service standard qui est exécuté en permanence et qui détecte une activité suspecte par rapport à des normes.

## Principe d'un HIDS
Dans notre cas nous avons réalisé un HIDS pour un serveur web dont le but était de détecter des intrusions via la modification des fichiers présent sur le serveur web pour la mise en ligne de différents sites internet. L’idée était d’avoir une partie gestion de l’HIDS avec un site en interne pour pouvoir lancer des analyses et également visualiser les différentes inspections ainsi que leurs retours et une partie en python qui réalise les différentes vérifications.

Le fonctionnement de l'HIDS repose sur le principe des empreintes des fichiers. Le but était d'obtenir et de stocker en base de données l'empreinte de tous les fichiers du serveur web à un instant T où l'on est sûr que les fichiers n'ont pas été corrompus ou modifiés pour pouvoir servir de référence pour les vérifications.

Lors d'une vérification, l'algorithme en python calcul les empreintes des fichiers présents sur le serveur, les compare aux empreintes stockées en base de données et vérifie la présence de différences. Si des différences sont détectées, une alerte indiquant le fichier est levée sur le site en interne.

## Réalisations

HIDS Gestion
* Mise en place d'un VPS (Virtual Private Server) et configuration en mode serveur web pour accéder au site de gestion de l'HIDS.
* Mise en place d'une base de données MySQL pour stocker les empreintes.
* Création d'un site en PHP avec Laravel pour la gestion de l'HIDS.

HIDS Python
* Création d'un programme en python pour la création des checksum.
* Création d'un programme en python pour la comparaison des checksum.
* Connexion à une base de données en python.

## Environnement

Python, Pycharm, PHP, Laravel, MySQL, VPS, Seveur Web, PhpMyAdmin
