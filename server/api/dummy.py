from django.db import connection

def dummy_user_add():
    user_data = [
        {"user_id": 1, "first_name": "John", "last_name": "Smith", "email": "John123@a.com", "password": "John123", "age": 20},
        {"user_id": 2, "first_name": "Jane", "last_name": "Doe", "email": "Jane123@a.com", "password": "Jane123", "age": 21},
        {"user_id": 3, "first_name": "Bob", "last_name": "Smith", "email": "Bob123@a.com", "password": "Bob123", "age": 22},
        {"user_id": 4, "first_name": "Alice", "last_name": "Doe", "email": "Alice@a.com", "password": "Alice123", "age": 23},
    ]
    sql = "INSERT INTO api_user (user_id, first_name, last_name, email, password, age) VALUES (%s, %s, %s, %s, %s, %s)"
    with connection.cursor() as cursor:
        for user in user_data:
            cursor.execute(sql, [user['user_id'], user['first_name'], user['last_name'], user['email'], user['password'], user['age']])
    return

    
def dummy_cuisine_add():
    cuisine_data = [
        {"cuisine_name": "Italian", "method": "Baking", "category": "Main Course"},
        {"cuisine_name": "Chinese", "method": "Stir Fry", "category": "Main Course"},
        {"cuisine_name": "Indian", "method": "Boiling", "category": "Main Course"},
        {"cuisine_name": "Mexican", "method": "Frying", "category": "Main Course"},
    ]
    sql = "INSERT INTO api_cuisine (cuisine_name, method, category) VALUES (%s, %s, %s)"
    with connection.cursor() as cursor:
        for cuisine in cuisine_data:
            cursor.execute(sql, [cuisine['cuisine_name'], cuisine['method'], cuisine['category']])
    return

def dummy_recipe_add():
    recipe_data = [
        {"recipe_id": 1, "cook_time": 45, "description": "Delicious pasta", "process": "Boil pasta...", "cuisine_name": "Italian"},
        {"recipe_id": 2, "cook_time": 30, "description": "Tasty noodles", "process": "Fry noodles...", "cuisine_name": "Chinese"},
        {"recipe_id": 3, "cook_time": 60, "description": "Spicy curry", "process": "Boil curry...", "cuisine_name": "Indian"},
        {"recipe_id": 4, "cook_time": 15, "description": "Yummy tacos", "process": "Fry tacos...", "cuisine_name": "Mexican"},
    ]
    sql = "INSERT INTO api_recipe (recipe_id, cook_time, description, process, cuisine_name) VALUES (%s, %s, %s, %s, %s)"
    with connection.cursor() as cursor:
        for recipe in recipe_data:
            cursor.execute(sql, [recipe['recipe_id'], recipe['cook_time'], recipe['description'], recipe['process'], recipe['cuisine_name']])
    return

def dummy_ingredient_add():
    ingredient_data = [
        {"ingredient_name": "Pasta", "type": "Grain", "calories": 200},
        {"ingredient_name": "Noodles", "type": "Grain", "calories": 250},
        {"ingredient_name": "Curry", "type": "Spice", "calories": 50},
        {"ingredient_name": "Tacos", "type": "Grain", "calories": 150},
    ]
    sql = "INSERT INTO api_ingredient (ingredient_name, type, calories) VALUES (%s, %s, %s)"
    with connection.cursor() as cursor:
        for ingredient in ingredient_data:
            cursor.execute(sql, [ingredient['ingredient_name'], ingredient['type'], ingredient['calories']])
    return

def dummy_review_add():
    review_data = [
        {"review_id": 1, "content": "Great pasta!", "user_id": 1, "recipe_id": 1},
        {"review_id": 2, "content": "Loved the noodles.", "user_id": 2, "recipe_id": 2},
        {"review_id": 3, "content": "Spicy curry.", "user_id": 3, "recipe_id": 3},
        {"review_id": 4, "content": "Yummy tacos.", "user_id": 4, "recipe_id": 4},
    ]
    sql = "INSERT INTO api_review (review_id, content, user_id, recipe_id) VALUES (%s, %s, %s, %s)"
    with connection.cursor() as cursor:
        for review in review_data:
            cursor.execute(sql, [review['review_id'], review['content'], review['user_id'], review['recipe_id']])
    return

def dummy_recipe_needs_ingredient_add():
    recipe_needs_ingredient_data = [
        {"recipe_id": 1, "ingredient_name": "Pasta"},
        {"recipe_id": 2, "ingredient_name": "Noodles"},
        {"recipe_id": 3, "ingredient_name": "Curry"},
        {"recipe_id": 4, "ingredient_name": "Tacos"},
    ]
    sql = "INSERT INTO api_recipe_needs_ingredient (recipe_id, ingredient_name) VALUES (%s, %s)"
    with connection.cursor() as cursor:
        for rni in recipe_needs_ingredient_data:
            cursor.execute(sql, [rni['recipe_id'], rni['ingredient_name']])
    return

def dummy_refrigerator_add():
    refrigerator_data = [
        {"user_id": 1, "created_at": "2021-01-01 00:00:00", "capacity": 300},
        {"user_id": 2, "created_at": "2021-01-02 00:00:00", "capacity": 350},
        {"user_id": 3, "created_at": "2021-01-03 00:00:00", "capacity": 400},
        {"user_id": 4, "created_at": "2021-01-04 00:00:00", "capacity": 450},
    ]
    sql = "INSERT INTO api_refrigerator (user_id, created_at, capacity) VALUES (%s, %s, %s)"
    with connection.cursor() as cursor:
        for refrigerator in refrigerator_data:
            cursor.execute(sql, [refrigerator['user_id'], refrigerator['created_at'], refrigerator['capacity']])
    return

def dummy_refrigerator_stores_ingredient_add():
    refrigerator_stores_ingredient_data = [
        {"refrigerator": 1, "ingredient_name": "Pasta"},
        {"refrigerator": 2, "ingredient_name": "Noodles"},
        {"refrigerator": 3, "ingredient_name": "Curry"},
        {"refrigerator": 4, "ingredient_name": "Tacos"},
    ]
    sql = "INSERT INTO api_refrigerator_stores_ingredient (refrigerator, ingredient_name) VALUES (%s, %s)"
    with connection.cursor() as cursor:
        for rsi in refrigerator_stores_ingredient_data:
            cursor.execute(sql, [rsi['refrigerator'], rsi['ingredient_name']])
    return
