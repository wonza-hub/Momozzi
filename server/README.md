# How To Start

1. pip install -r requirements.txt
2. change .env.example to .env and fill in the values
3. create schema "momozzi" in mysql
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py runserver {port number}




# Endpoints


## User

### /api/user
Get all users

### /api/user/{id}
Get user by id

### /api/user/add/{id}/{first_name}/{last_name}/{age}
Add user

### /api/user/delete/{id}
Delete user by id

### /api/user/update/{id}/{first_name}/{last_name}/{age}
Update user by id


## Cuisine

### /api/cuisine
Get all cuisines

### /api/cuisine/{cuisine_name}
Get cuisine by name

### /api/cuisine/add/{cuisine_name}/{method}/{category}
Add cuisine

### /api/cuisine/delete/{cuisine_name}
Delete cuisine by name

### /api/cuisine/update/{cuisine_name}/{method}/{category}
Update cuisine by name


## Recipe

### /api/recipe
Get all recipes

### /api/recipe/{id}
Get recipe by id

### /api/recipe/add/{id}/{cook_time}/{description}/{process}/{cuisine_name}
Add recipe

### /api/recipe/delete/{id}
Delete recipe by id

### /api/recipe/update/{id}/{cook_time}/{description}/{process}/{cuisine_name}
Update recipe by id


## Ingredient

