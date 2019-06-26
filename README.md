# Prusa

Setting up Environment

    We are using pipenv for the environment
    
    pip install pipenv
    pipenv --python `which python3` shell
    pipenv install #it will install all the requirements
    

Database setup

    You just need to run migrate
    
    python manage.py migrate
    
Collect Static files

    python manage.py collectstatic

Create Super user

    python manage.py createsuperuser
    