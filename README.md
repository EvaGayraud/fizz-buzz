# FizzBuzz Backend

Ce projet implémente une API FizzBuzz en Python.

## Prérequis

*   Docker
*   Docker Compose

## Installation et Lancement avec Docker

Ce projet est configuré pour fonctionner facilement avec Docker.

### Lancer l'application

Pour construire et lancer le conteneur :
```
docker compose build
docker compose up
```

Pour lancer les tests dans le conteneur :
```pytest tests/```

L'application sera accessible sur `http://localhost:8000`.

### Arrêter l'application

Pour arrêter les conteneurs :
```docker compose down```


## Structure du Projet

*   `fizz_buzz/` : Code source de l'application.
*   `tests/` : Tests unitaires et d'intégration.
*   `Dockerfile` : Configuration pour la création de l'image Docker.
*   `docker-compose.yml` : Configuration pour l'orchestration des conteneurs.

Le projet a été développé en suivant les principes de la Clean Architecture.
Cependant, il n’intègre pas réellement d’entités, ce qui s’éloigne un peu de l’esprit de ce modèle : en général,
dès lors que l’on définit un domaine, on définit aussi des entités qui le représentent.

C’est ainsi que je structure mes projets aujourd’hui. J’ai appliqué cette approche pour le test, mais ce n’était
peut-être pas le choix le plus adapté au contexte.

Voici une autre architecture possible :
```
/fizz_buzz
    /api
        /v1
            /endpoints
                routes.py
                models.py
    /core
        config.py
        stats.py
    main.py
```
