from django.db import connection

def dummy_user_add():
    user_data = [
        {"user_id": 1, "first_name": "John", "last_name": "Doe", "age": 30},
        {"user_id": 2, "first_name": "Jane", "last_name": "Doe", "age": 28},
    ]
    sql = "INSERT INTO appname_user (user_id, first_name, last_name, age) VALUES (%s, %s, %s, %s)"
    with connection.cursor() as cursor:
        for user in user_data:
            cursor.execute(sql, [user['user_id'], user['first_name'], user['last_name'], user['age']])
    return "Dummy users added successfully."

def dummy_cuisine_add():
    cuisine_data = [
        {"cuisine_name": "Italian", "method": "Baking", "category": "Main Course"},
        {"cuisine_name": "Chinese", "method": "Stir Fry", "category": "Main Course"},
    ]
    sql = "INSERT INTO appname_cuisine (cuisine_name, method, category) VALUES (%s, %s, %s)"
    with connection.cursor() as cursor:
        for cuisine in cuisine_data:
            cursor.execute(sql, [cuisine['cuisine_name'], cuisine['method'], cuisine['category']])
    return "Dummy cuisines added successfully."

