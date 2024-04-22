# About project

This project is a web application developed with Django and utilizes a PostgreSQL database to manage quotes and author details. It features an integration with OpenAI, which automatically generates new quotes every 12 hours and stores them in the database. The application allows users to register, enabling them to submit new quotes and author information.

# Technologies
- Django 
- Postgres
- OpenAI



# Get started

Getting Started

Clone the Repository:
git clone https://github.com/Olena-24/HW-10.git

Navigate to the Project Folder:
cd quotes_project

Activate the Poetry Environment:
poetry shell

Install Dependencies:
poetry install

Execute Database Migrations:
python manage.py makemigrations
python manage.py migrate

Launch the Server:
python manage.py runserver --noreload