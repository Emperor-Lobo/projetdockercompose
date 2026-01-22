# Docker Compose Project – ex01 → ex04

Ce dépôt contient une suite de 4 exercices Docker Compose illustrant la montée en complexité d’une application web Dockerisée, depuis une architecture simple jusqu’à une stack complète sécurisée avec réseaux isolés, Tor et PostgreSQL.

Chaque exercice est indépendant et possède son propre :

docker-compose.yml

Makefile

.env

README.md

Les exercices peuvent être exécutés séparément.

---

# Structure du dépôt

projetdockercompose/
├── ex01/ # Backend + Frontend simple
├── ex02/ # Ajout d’une base de données (SQLite)
├── ex03/ # Ajout de Tor + réseaux Docker
├── ex04/ # Architecture complète (Tor + PostgreSQL + PgAdmin)

---

# Objectifs pédagogiques

| Exercice | Contenu                                                                          |
| -------- | -------------------------------------------------------------------------------- |
| ex01     | Dockerisation d’un backend Flask et d’un frontend Nginx                          |
| ex02     | Ajout d’une base de données persistante                                          |
| ex03     | Séparation réseau + routage du backend via Tor                                   |
| ex04     | Stack DevOps complète : Tor, PostgreSQL, PgAdmin, réseaux isolés, .env, Makefile |

---

# Lancer un exercice

Chaque exercice est autonome.

Exemple avec ex04 :

cd ex04
make up

Pour arrêter :

make down

---

# Nettoyage

Chaque exercice possède son propre Makefile avec les règles suivantes :
| Commande       | Effet                                                                                        |
| -------------- | -------------------------------------------------------------------------------------------- |
| make purge_bdd | Supprime uniquement le volume de la base de données                                          |
| make purge_all | Supprime conteneurs, images, volumes, réseaux et fichiers temporaires, puis relance la stack |

---

# Sécurité et bonnes pratiques

Dans ex04, toutes les données sensibles sont stockées dans des fichiers .env :

backend.env

frontend.env

postgres.env

pgadmin.env

Aucune variable sensible n’est écrite en dur dans les fichiers Docker ou Docker Compose.

PgAdmin est automatiquement configuré via le fichier :
docker/pgadmin_servers.json

---

# Accès aux services (ex04)
| Service     | URL                                            |
| ----------- | ---------------------------------------------- |
| Frontend    | [http://localhost:3000](http://localhost:3000) |
| Backend API | [http://localhost:5000](http://localhost:5000) |
| PgAdmin     | [http://localhost:5050](http://localhost:5050) |
