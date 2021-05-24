# Blog Project of the "Python Django the Practical Guide" course

Simple Django project to get familiar with models, migrations, admin registration of models, etc.

It also uses Pipenv + Virtualentwrapper + Virtualenvs to manage virtual environments.

To run it on your machine, please, first install Pipenv, then install dependencies from the project folder with `pipenv install`.
Once all dependencies have been installed, to run the project for the first time you'll need to:

1. `python manage.py migrate`
2. `python manage.py runserver`

## SECURITY WARNING:

This project is meant to be run on your local machine, for learning purposes only. Secret keys and other specific security settings should not be exposed but rather concealed with appropriate operations like the use of specific to each environment `.env` files.
