# AYOMI TEST

Faire un site en suivant les instructions suivantes :

•  Nous souhaitons une page permettant à un utilisateur de se connecter.
•  Une fois connecté, l'utilisateur accède à une page pour afficher / modifier ses informations.
•  En cliquant sur "Modifier ses informations", on veut avoir une modale qui s'ouvre.
•  Dans cette modale,  on veut un input permettant de modifier son adresse email, ainsi qu'un bouton "enregistrer". A l'appui de ce bouton, l'adresse email sera modifiée dans la base de données et sur la page principale sans rechargement de la page.
•  Le code python doit être écrit en Orienté Objet.
•  Une base de donnée doit-être incluse.
•  On utilisera Django, Python et Bootstrap. Vous êtes libre d'utiliser d'autres outils ou Frameworks selon vos préférences.
•  Nous aimerions le rendu sous Git avec la doc pour faire tout fonctionner

Vous devrez utiliser Docker pour le containériser (file+ compose).

- Ouvrir l'application Docker sur votre pc

sur le shell de votre ordinateur, cloner le répertoire:  
```shell
git clone https://github.com/iabdelkerim/ayomi-test.git
cd ayomi-test
docker-compose up
```
- Utiliser l'environnement virtuel et lancer le conteneur Docker:
```shell
source env/bin/activate
docker-compose up
```

- Dans votre navigateur, accédez au site via l'url http://localhost:8000/

