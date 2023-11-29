from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
import json
from .dummy import dummy_user_add, dummy_cuisine_add, dummy_recipe_add, dummy_ingredient_add, dummy_review_add, dummy_recipe_needs_ingredient_add, dummy_refrigerator_add, dummy_refrigerator_stores_ingredient_add

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

### User ###
def get_all_users(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM api_user")
        users = cursor.fetchall()
        users = json.dumps(users)
        return HttpResponse(users)
    
def get_user(request, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM api_user WHERE user_id = %s", [user_id])
        user = cursor.fetchone()
        user = json.dumps(user)
        return HttpResponse(user)

def post_user(request, user_id, first_name, last_name, age):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO api_user VALUES (%s, %s, %s, %s)", [user_id, first_name, last_name, age])
        return HttpResponse("User added")

def delete_user(request, user_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM api_user WHERE user_id = %s", [user_id])
        return HttpResponse("User deleted")

def update_user(request, user_id, first_name, last_name, age):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE api_user SET first_name = %s, last_name = %s, age = %s WHERE user_id = %s", [first_name, last_name, age, user_id])
        return HttpResponse("User updated")

### Cuisine ###
def get_all_cuisines(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM api_cuisine")
        cuisines = cursor.fetchall()
        cuisines = json.dumps(cuisines)
        return HttpResponse(cuisines)

def get_cuisine(request, cuisine_name):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM api_cuisine WHERE cuisine_name = %s", [cuisine_name])
        cuisine = cursor.fetchone()
        cuisine = json.dumps(cuisine)
        return HttpResponse(cuisine)

def post_cuisine(request, cuisine_name, method, category):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO api_cuisine VALUES (%s, %s, %s)", [cuisine_name, method, category])
        return HttpResponse("Cuisine added")

def delete_cuisine(request, cuisine_name):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM api_cuisine WHERE cuisine_name = %s", [cuisine_name])
        return HttpResponse("Cuisine deleted")

def update_cuisine(request, cuisine_name, method, category):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE api_cuisine SET method = %s, category = %s WHERE cuisine_name = %s", [method, category, cuisine_name])
        return HttpResponse("Cuisine updated")

### Recipe ###
def get_all_recipes(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM api_recipe")
        recipes = cursor.fetchall()
        recipes = json.dumps(recipes)
        return HttpResponse(recipes)

def get_recipe(request, recipe_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM api_recipe WHERE recipe_id = %s", [recipe_id])
        recipe = cursor.fetchone()
        recipe = json.dumps(recipe)
        return HttpResponse(recipe)

def post_recipe(request, recipe_id, cook_time, description, process, cuisine_name):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO api_recipe VALUES (%s, %s, %s, %s, %s)", [recipe_id, cook_time, description, process, cuisine_name])
        return HttpResponse("Recipe added")

def delete_recipe(request, recipe_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM api_recipe WHERE recipe_id = %s", [recipe_id])
        return HttpResponse("Recipe deleted")

def update_recipe(request, recipe_id, cook_time, description, process, cuisine_name):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE api_recipe SET cook_time = %s, description = %s, process = %s, cuisine_name = %s WHERE recipe_id = %s", [cook_time, description, process, cuisine_name, recipe_id])
        return HttpResponse("Recipe updated")

### Ingredient ###
def get_all_ingredients(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM api_ingredient")
        ingredients = cursor.fetchall()
        ingredients = json.dumps(ingredients)
        return HttpResponse(ingredients)

def get_ingredient(request, ingredient_name):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM api_ingredient WHERE ingredient_name = %s", [ingredient_name])
        ingredient = cursor.fetchone()
        ingredient = json.dumps(ingredient)
        return HttpResponse(ingredient)

def post_ingredient(request, ingredient_name, type, calories):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO api_ingredient VALUES (%s, %s, %s)", [ingredient_name, type, calories])
        return HttpResponse("Ingredient added")

def delete_ingredient(request, ingredient_name):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM api_ingredient WHERE ingredient_name = %s", [ingredient_name])
        return HttpResponse("Ingredient deleted")

def update_ingredient(request, ingredient_name, type, calories):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE api_ingredient SET type = %s, calories = %s WHERE ingredient_name = %s", [type, calories, ingredient_name])
        return HttpResponse("Ingredient updated")

### Review ###
def get_all_reviews(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM api_review")
        reviews = cursor.fetchall()
        reviews = json.dumps(reviews)
        return HttpResponse(reviews)

def get_review(request, review_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM api_review WHERE review_id = %s", [review_id])
        review = cursor.fetchone()
        review = json.dumps(review)
        return HttpResponse(review)

def post_review(request, review_id, content, user_id, recipe_id):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO api_review VALUES (%s, %s, %s, %s)", [review_id, content, user_id, recipe_id])
        return HttpResponse("Review added")

def delete_review(request, review_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM api_review WHERE review_id = %s", [review_id])
        return HttpResponse("Review deleted")

def update_review(request, review_id, content, user_id, recipe_id):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE api_review SET content = %s, user_id = %s, recipe_id = %s WHERE review_id = %s", [content, user_id, recipe_id, review_id])
        return HttpResponse("Review updated")

### Recipe Needs Ingredient ###
def get_all_recipe_needs_ingredients(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM api_recipe_needs_ingredient")
        recipe_needs_ingredients = cursor.fetchall()
        return HttpResponse(recipe_needs_ingredients)
        return HttpResponse(recipe_needs_ingredients)

def get_recipe_needs_ingredient(request, recipe_id, ingredient_name):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM api_recipe_needs_ingredient WHERE recipe_id = %s AND ingredient_name = %s", [recipe_id, ingredient_name])
        recipe_needs_ingredient = cursor.fetchone()
        recipe_needs_ingredient = json.dumps(recipe_needs_ingredient)
        return HttpResponse(recipe_needs_ingredient)

def post_recipe_needs_ingredient(request, recipe_id, ingredient_name):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO api_recipe_needs_ingredient VALUES (%s, %s)", [recipe_id, ingredient_name])
        return HttpResponse("Recipe needs ingredient added")

def delete_recipe_needs_ingredient(request, recipe_id, ingredient_name):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM api_recipe_needs_ingredient WHERE recipe_id = %s AND ingredient_name = %s", [recipe_id, ingredient_name])
        return HttpResponse("Recipe needs ingredient deleted")

def update_recipe_needs_ingredient(request, recipe_id, ingredient_name):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE api_recipe_needs_ingredient SET recipe_id = %s WHERE ingredient_name = %s", [recipe_id, ingredient_name])
        return HttpResponse("Recipe needs ingredient updated")

### Refrigerator ###
def get_all_refrigerators(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM api_refrigerator")
        refrigerators = cursor.fetchall()
        return HttpResponse(refrigerators)
        return HttpResponse(refrigerators)

def get_refrigerator(request, user_id, created_at):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM api_refrigerator WHERE user_id = %s AND created_at = %s", [user_id, created_at])
        refrigerator = cursor.fetchone()
        refrigerator = json.dumps(refrigerator)
        return HttpResponse(refrigerator)

def post_refrigerator(request, user_id, created_at, capacity):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO api_refrigerator VALUES (%s, %s, %s)", [user_id, created_at, capacity])
        return HttpResponse("Refrigerator added")

def delete_refrigerator(request, user_id, created_at):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM api_refrigerator WHERE user_id = %s AND created_at = %s", [user_id, created_at])
        return HttpResponse("Refrigerator deleted")

def update_refrigerator(request, user_id, created_at, capacity):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE api_refrigerator SET capacity = %s WHERE user_id = %s AND created_at = %s", [capacity, user_id, created_at])
        return HttpResponse("Refrigerator updated")

### Refrigerator Stores Ingredient ###
def get_all_refrigerator_stores_ingredients(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM api_refrigerator_stores_ingredient")
        refrigerator_stores_ingredients = cursor.fetchall()
        refrigerator_stores_ingredients = json.dumps(refrigerator_stores_ingredients)
        return HttpResponse(refrigerator_stores_ingredients)

def get_refrigerator_stores_ingredient(request, refrigerator, ingredient_name):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM api_refrigerator_stores_ingredient WHERE refrigerator = %s AND ingredient_name = %s", [refrigerator, ingredient_name])
        refrigerator_stores_ingredient = cursor.fetchone()
        refrigerator_stores_ingredient = json.dumps(refrigerator_stores_ingredient)
        return HttpResponse(refrigerator_stores_ingredient)

def post_refrigerator_stores_ingredient(request, refrigerator, ingredient_name):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO api_refrigerator_stores_ingredient VALUES (%s, %s)", [refrigerator, ingredient_name])
        return HttpResponse("Refrigerator stores ingredient added")

def delete_refrigerator_stores_ingredient(request, refrigerator, ingredient_name):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM api_refrigerator_stores_ingredient WHERE refrigerator = %s AND ingredient_name = %s", [refrigerator, ingredient_name])
        return HttpResponse("Refrigerator stores ingredient deleted")

def update_refrigerator_stores_ingredient(request, refrigerator, ingredient_name):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE api_refrigerator_stores_ingredient SET refrigerator = %s WHERE ingredient_name = %s", [refrigerator, ingredient_name])
        return HttpResponse("Refrigerator stores ingredient updated")

### Dummy ###
def dummy_add(request):
    dummy_user_add()
    dummy_cuisine_add()
    dummy_recipe_add()
    dummy_ingredient_add()
    dummy_review_add()
    dummy_recipe_needs_ingredient_add()
    dummy_refrigerator_add()
    dummy_refrigerator_stores_ingredient_add()
    return HttpResponse("Dummy data added")

### Clear ###
def clear_all(request):
    with connection.cursor() as cursor:
        # Delete from child tables first
        cursor.execute("DELETE FROM api_review")
        cursor.execute("DELETE FROM api_recipe_needs_ingredient")
        cursor.execute("DELETE FROM api_refrigerator_stores_ingredient")

        # Then delete from parent tables
        cursor.execute("DELETE FROM api_recipe")
        cursor.execute("DELETE FROM api_cuisine")
        cursor.execute("DELETE FROM api_ingredient")
        cursor.execute("DELETE FROM api_refrigerator")
        cursor.execute("DELETE FROM api_user")

        return HttpResponse("All data cleared")
