# Chatcook

Thomas Clouet - Chama El Majeny - Julie James - Gabriel Jolly


- [Installation et lancement](#install)
    - [Prérequis](#prerequis)
    - [Commandes](#commandes)
    - [Lancer une discussion](#serv)
    - [Lancer la page web](#web)
- [Utilisation](#utilisation)
    - [Salutation](#salut)
    - [Demande de recette](#recette)

## Installation et lancement <a name="install"></a>

### Prérequis <a name="prerequis"></a>

Avoir un venv python3 avec Rasa d'installé :

-   https://rasa.com/docs/rasa/installation/environment-set-up/
-   https://rasa.com/docs/rasa/installation/installing-rasa-open-source

Vérifier que python3 est bien installé (version 3.9 recommandée) :

```
python3 --version
```

Mettre en place en environnement virtuel :

```
python3.9 -m venv ./venv
.\venv\Scripts\activate
```

Installer Rasa :

```
pip3 install rasa
```

Installer Googletrans :

```
pip install googletrans==4.0.0-rc1
```

### Commandes <a name="commandes"></a>

Liste des commandes shell à utiliser pour faire fonctionner Rasa :

-   https://rasa.com/docs/rasa/command-line-interface
-   https://rasa.com/docs/rasa/domain/

### Lancer une discussion <a name="serv"></a>

Si le modèle a changé, lancer l'apprentissage :

```
rasa train
```

Puis, il faut lancer le serveur d'actions :

```
rasa run actions
```

Enfin executer le shell Rasa dans un autre terminal que le server pour commencer une discussion :

```
rasa shell
```

### Lancer la page web <a name="web"></a>

```
rasa run --enable-api --cors "*"
```

## Utilisation <a name="utilisation"></a>

### Salutation <a name="salut"></a>

La communication la plus simple reste de dire bonjour, un simple "**Bonjour**" vous donnera une réponse instantannée du bot.

### Demande de recette <a name="recette"></a>

Pour obtenir une recette il suffit de demander au bot un type de recette, par exemple :

- Je veux cuisine une ratatouille
- Comment cuisiner des lasagnes

Le bot va ensuite vous proposer diverse recette, vous pourrez la sélectionnant en entrant le numéro de la recette. Il va donc vous donner la liste d'ingrédients. Pour obtenir les étapes complètes de la recette, il faudra répondre à sa question "Voulez-vous voir la recette complète?".