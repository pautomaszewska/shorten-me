## Shorten me

### Info
URL shortener created as a recruitment task. Demo: https://url-shorten-me.herokuapp.com/

### Technologies
* Python 3.6
* Django 2.2
* Bootstrap 4
* PostgreSQL

### Functions
* user enters an URL to shorten
* the app generates shortened URL in <domain>/<abbreviation> format
* the user is redirected to the original address after clicking the shortened URL
* the admin can view all the URLs with their abbreviations

### Installation
* clone repository to your computer
* create virtual environment by running:
```
virtualenv -p python3 env
```
* activate virtual environment by running:
```
source env/bin/activate
```
* install requirements:
```
pip install -r requirements.txt
```
* run migrations:
```
python manage.py makemigrations
python manage.py migrate
```
* run server:
```
python manage.py runserver
```  
* create superuser to view all data as admin:
```
python manage.py createsuperuser
```
