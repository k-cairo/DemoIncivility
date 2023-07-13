# Incivility

Ce projet est un outil d'aide aux ensaignants pour la gestion des élèves au quotidien et de gérer les absences et les 
retards des élèves mais également de réunir sur un même document les incivilités dont ils font preuve. 

Tout cela est à destination des familles et favorise le travail en équipe entre les enseignants et les parents.

Ce projet est disponible en suivant ce lien : https://demoincivilite.pythonanywhere.com/

## Installation

1. Cloner le projet

    ```bash
   https://github.com/k-cairo/Incivility.git
    ```
   
2. Créer un environnement virtuel afin d'y installer les dépendances

    ```bash
    python -m venv env
    source env/bin/activate
     ```

3. Installer les dépendances

    ```bash
    (env)$ pip -r install requirements.txt
    ```
    A noter le ```(env)``` qui indique que l'on est bien dans l'environnement virtuel.


5. Appliquer les migrations

    ```bash
    (env)$ cd {{ nom_du_projet }}}
    (env)$ python manage.py makemigrations
    (env)$ python manage.py migrate
    ```

6. Créer un super utilisateur

    ```bash
    (env)$ python manage.py createsuperuser
    ```

7. Lancer le serveur

    ```bash
    (env)$ python manage.py runserver
    ```
