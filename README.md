## Application Name
Photo hub
## About the application
An application that allows you to put and describe your personal photolife

## Author
Eugene(Eugeneiregi)
## Setup and Installations
Fork and clone this repository to your local machine

Obuntu commands:

- git clone ("https://github.com/Eugeneiregi/Gallery-hub")
#### Assumptions
1. You are using Ubuntu Operating system
2. You have knowledge on virtual environment and Django framework
3. Knowledge on database migrations
## What you need
* Python version 3.6 Installation guide
* postgresql database
## B.D.D
## BDD
As a user of the application you will be able to:

* view different photos that interest you.
* click on a single photo to expand it and also view the details of the photo.
* search for different categories of photos.{use search term travel,wildlife and food to get a result}
* copy a link to the photo to share with your friends.





## Installation
- set up a virtual environment using the following command
- python3 -m venv  virtual
And activate virtual
[source virtual/bin/activate]



Install the requirements using:
- pip install -r requirements.txt/ pip freeze > requirements.txt
- create a .env file and add
- SECRET_KEY='<random-string>'
- DEBUG=True
- ALLOWED_HOSTS='*'
- DATABASE_URL='postgres://databaseowner:password@localhost/databasename'
- create a database using postgresql(recommend)
* CREATE DATABASE <your-database-name>
- create a migration using the following command
- python3 manage.py makemigrations
- python manage.py migrate

- create a super user for admin account
* python 3.6 manage.py createsuperuser
* add your password and username , email is not a must.

## To run user :
- python3 manage.py runserver
- navigate to admin by adding /admin to your local host url like so :
127.0.0.1:8000/admin
## Running the tests
python3 manage.py tests
## Technologies Used
* Html and CSS
* Python
* Bootdstrap 3
* Django - The web framework used
* JQUERY
