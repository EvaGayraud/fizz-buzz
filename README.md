# FizzBuzz Backend

Ce projet implémente une API FizzBuzz en Python.

## Prérequis

*   Docker
*   Docker Compose

## Installation et Lancement avec Docker

Ce projet est configuré pour fonctionner facilement avec Docker.

### Lancer l'application

Pour construire et lancer les conteneurs :
```
docker compose build
docker compose up
```


L'application sera accessible sur `http://localhost:8000`.

### Arrêter l'application

Pour arrêter les conteneurs :


## Structure du Projet

*   `fizz_buzz/` : Code source de l'application.
*   `tests/` : Tests unitaires et d'intégration.
*   `Dockerfile` : Configuration pour la création de l'image Docker.
*   `docker-compose.yml` : Configuration pour l'orchestration des conteneurs.
