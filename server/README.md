# How To Start

1. pip install -r requirements.txt
2. change .env.example to .env and fill in the values
3. create schema "momozzi" in mysql
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py runserver {port number}




# Endpoints

## /api

### /api/user
GET: get all users
POST: create a user
{
    user_id : int
    first_name : string
    last_name : string
    age : int
}

...
