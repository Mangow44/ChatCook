## Prérequis :

Avoir un venv python3 avec Rasa d'installé :

-   https://rasa.com/docs/rasa/installation/environment-set-up/
-   https://rasa.com/docs/rasa/installation/installing-rasa-open-source

Vérifier que python3 est bien installé (version 3.9 recommandée) :

-   python3 --version

Mettre en place en environnement virtuel :

-   python3.9 -m venv ./venv
-   .\venv\Scripts\activate

Installer Rasa :

-   pip3 install rasa

## Commandes :

Liste des commandes shell à utiliser pour faire fonctionner Rasa :

-   https://rasa.com/docs/rasa/command-line-interface
-   https://rasa.com/docs/rasa/domain/

## Actions customisées :

Si le modèle a changé, lancer l'apprentissage :

-   rasa train

Puis, il faut lancer le serveur d'actions :

-   rasa run actions

Enfin executer le shell Rasa :

-   rasa shell

## Lancer la page web :

-   rasa run --enable-api --cors "\*"
