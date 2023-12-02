from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
import json
from django.views.decorators.csrf import csrf_exempt
from .dummy import dummy_user_add, dummy_cuisine_add, dummy_recipe_add, dummy_ingredient_add, dummy_review_add, dummy_recipe_needs_ingredient_add, dummy_refrigerator_add, dummy_refrigerator_stores_ingredient_add

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

### User ###
def user(request):    
    if request.method == "GET":
        user_id = request.GET.get("user_id")
        email = request.GET.get("email")
        if user_id is None and email is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_user")
                rows = cursor.fetchall()
                columns = [col[0] for col in cursor.description]
                users = [dict(zip(columns, row)) for row in rows]
                return JsonResponse(users, safe=False)
            
        elif user_id is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_user WHERE email = %s", [email])
                rows = cursor.fetchall()
                columns = [col[0] for col in cursor.description]
                users = [dict(zip(columns, row)) for row in rows]
                return JsonResponse(users, safe=False)
            
        elif email is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_user WHERE user_id = %s", [user_id])
                rows = cursor.fetchall()
                columns = [col[0] for col in cursor.description]
                users = [dict(zip(columns, row)) for row in rows]
                return JsonResponse(users, safe=False)
            
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_user WHERE user_id = %s AND email = %s", [user_id, email])
                rows = cursor.fetchall()
                columns = [col[0] for col in cursor.description]
                users = [dict(zip(columns, row)) for row in rows]
                return JsonResponse(users, safe=False)
    
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            user_id = data["user_id"]
            first_name = data["first_name"]
            last_name = data["last_name"]
            age = data["age"]
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO api_user VALUES (%s, %s, %s, %s)", [user_id, first_name, last_name, age])
                rows = cursor.fetchall()
                columns = [col[0] for col in cursor.description]
                users = [dict(zip(columns, row)) for row in rows]
                return JsonResponse(users, safe=False)
        except Exception as e:
            return HttpResponse(e)
    
    elif request.method == "DELETE":
        try:
            data = json.loads(request.body)
            user_id = data["user_id"]
            
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM api_user WHERE user_id = %s", [user_id])
                return HttpResponse("User deleted")
        except Exception as e:
            return HttpResponse(e)
    
    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
            user_id = data["user_id"]
            first_name = data["first_name"]
            last_name = data["last_name"]
            age = data["age"]
            
            with connection.cursor() as cursor:
                cursor.execute("UPDATE api_user SET first_name = %s, last_name = %s, age = %s WHERE user_id = %s", [first_name, last_name, age, user_id])
                return HttpResponse("User updated")
        except Exception as e:
            return HttpResponse(e)

@csrf_exempt
def user_login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data["email"]
            password = data["password"]
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_user WHERE email = %s AND password = %s", [email, password])
                rows = cursor.fetchall()
                columns = [col[0] for col in cursor.description]
                users = [dict(zip(columns, row)) for row in rows]
                user = users[0] if len(users) > 0 else None
                
                if user:
                    return JsonResponse(user, safe=False)
                else:
                    return HttpResponseForbidden("Invalid email or password")
        except Exception as e:
            return HttpResponse(e)
        

### Cuisine ###
def cuisine(request):
    if request.method == "GET":
        cuisine_name = request.GET.get("cuisine_name")
        if cuisine_name is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_cuisine")
                cuisines = cursor.fetchall()
                cuisines = json.dumps(cuisines)
                return HttpResponse(cuisines)
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_cuisine WHERE cuisine_name = %s", [cuisine_name])
                cuisine = cursor.fetchall()
                cuisine = json.dumps(cuisine)
                return HttpResponse(cuisine)
    
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            cuisine_name = data["cuisine_name"]
            method = data["method"]
            category = data["category"]
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO api_cuisine VALUES (%s, %s, %s)", [cuisine_name, method, category])
                return HttpResponse("Cuisine added")
        except Exception as e:
            return HttpResponse(e)
    
    elif request.method == "DELETE":
        try:
            data = json.loads(request.body)
            cuisine_name = data["cuisine_name"]
            
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM api_cuisine WHERE cuisine_name = %s", [cuisine_name])
                return HttpResponse("Cuisine deleted")
        except Exception as e:
            return HttpResponse(e)
    
    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
            cuisine_name = data["cuisine_name"]
            method = data["method"]
            category = data["category"]
            
            with connection.cursor() as cursor:
                cursor.execute("UPDATE api_cuisine SET method = %s, category = %s WHERE cuisine_name = %s", [method, category, cuisine_name])
                return HttpResponse("Cuisine updated")
        except Exception as e:
            return HttpResponse(e)

### Recipe ###
def recipe(request):
    if request.method == "GET":
        recipe_id = request.GET.get("recipe_id")
        if recipe_id is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_recipe")
                recipes = cursor.fetchall()
                recipes = json.dumps(recipes)
                return HttpResponse(recipes)
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_recipe WHERE recipe_id = %s", [recipe_id])
                recipe = cursor.fetchall()
                recipe = json.dumps(recipe)
                return HttpResponse(recipe)
    
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            recipe_id = data["recipe_id"]
            cook_time = data["cook_time"]
            description = data["description"]
            process = data["process"]
            cuisine_name = data["cuisine_name"]
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO api_recipe VALUES (%s, %s, %s, %s, %s)", [recipe_id, cook_time, description, process, cuisine_name])
                return HttpResponse("Recipe added")
        except Exception as e:
            return HttpResponse(e)
    
    elif request.method == "DELETE":
        try:
            data = json.loads(request.body)
            recipe_id = data["recipe_id"]
            
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM api_recipe WHERE recipe_id = %s", [recipe_id])
                return HttpResponse("Recipe deleted")
        except Exception as e:
            return HttpResponse(e)
    
    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
            recipe_id = data["recipe_id"]
            cook_time = data["cook_time"]
            description = data["description"]
            process = data["process"]
            cuisine_name = data["cuisine_name"]
            
            with connection.cursor() as cursor:
                cursor.execute("UPDATE api_recipe SET cook_time = %s, description = %s, process = %s, cuisine_name = %s WHERE recipe_id = %s", [cook_time, description, process, cuisine_name, recipe_id])
                return HttpResponse("Recipe updated")
        except Exception as e:
            return HttpResponse(e)

def recipe_search(request):
    if request.method == "GET":
        keyword = request.GET.get("keyword")
        if keyword is None:
            return HttpResponse("No keyword")
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_recipe WHERE description LIKE %s", ["%" + keyword + "%"])
                recipes = cursor.fetchall()
                recipes = json.dumps(recipes)
                return HttpResponse(recipes)
            
def recipe_search_by_category(request):
    if request.method == "GET":
        category = request.GET.get("category")
        if category is None:
            return HttpResponse("No category")
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_recipe WHERE cuisine_name IN (SELECT cuisine_name FROM api_cuisine WHERE category = %s)", [category])
                recipes = cursor.fetchall()
                recipes = json.dumps(recipes)
                return HttpResponse(recipes)

def recipe_search_by_method(request):
    if request.method == "GET":
        method = request.GET.get("method")
        if method is None:
            return HttpResponse("No method")
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_recipe WHERE cuisine_name IN (SELECT cuisine_name FROM api_cuisine WHERE method = %s)", [method])
                recipes = cursor.fetchall()
                recipes = json.dumps(recipes)
                return HttpResponse(recipes)


### Ingredient ###
def ingredient(request):
    if request.method == "GET":
        ingredient_name = request.GET.get("ingredient_name")
        if ingredient_name is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_ingredient")
                ingredients = cursor.fetchall()
                ingredients = json.dumps(ingredients)
                return HttpResponse(ingredients)
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_ingredient WHERE ingredient_name = %s", [ingredient_name])
                ingredient = cursor.fetchall()
                ingredient = json.dumps(ingredient)
                return HttpResponse(ingredient)
    
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            ingredient_name = data["ingredient_name"]
            type = data["type"]
            calories = data["calories"]
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO api_ingredient VALUES (%s, %s, %s)", [ingredient_name, type, calories])
                return HttpResponse("Ingredient added")
        except Exception as e:
            return HttpResponse(e)
    
    elif request.method == "DELETE":
        try:
            data = json.loads(request.body)
            ingredient_name = request.POST["ingredient_name"]
            
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM api_ingredient WHERE ingredient_name = %s", [ingredient_name])
                return HttpResponse("Ingredient deleted")
        except Exception as e:
            return HttpResponse(e)
    
    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
            ingredient_name = data["ingredient_name"]
            type = data["type"]
            calories = data["calories"]
            
            with connection.cursor() as cursor:
                cursor.execute("UPDATE api_ingredient SET type = %s, calories = %s WHERE ingredient_name = %s", [type, calories, ingredient_name])
                return HttpResponse("Ingredient updated")
        except Exception as e:
            return HttpResponse(e)


### Review ###
def review(request):
    if request.method == "GET":
        review_id = request.GET.get("review_id")
        if review_id is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_review")
                reviews = cursor.fetchall()
                reviews = json.dumps(reviews)
                return HttpResponse(reviews)
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_review WHERE review_id = %s", [review_id])
                review = cursor.fetchall()
                review = json.dumps(review)
                return HttpResponse(review)
    
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            review_id = data["review_id"]
            content = data["content"]
            user_id = data["user_id"]
            recipe_id = data["recipe_id"]
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO api_review VALUES (%s, %s, %s, %s)", [review_id, content, user_id, recipe_id])
                return HttpResponse("Review added")
        except Exception as e:
            return HttpResponse(e)
    
    elif request.method == "DELETE":
        try:
            data = json.loads(request.body)
            review_id = data["review_id"]
            
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM api_review WHERE review_id = %s", [review_id])
                return HttpResponse("Review deleted")
        except Exception as e:
            return HttpResponse(e)
    
    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
            review_id = data["review_id"]
            content = data["content"]
            user_id = data["user_id"]
            recipe_id = data["recipe_id"]
            
            with connection.cursor() as cursor:
                cursor.execute("UPDATE api_review SET content = %s, user_id = %s, recipe_id = %s WHERE review_id = %s", [content, user_id, recipe_id, review_id])
                return HttpResponse("Review updated")
        except Exception as e:
            return HttpResponse(e)



### Recipe Needs Ingredient ###
def recipe_needs_ingredient(request):
    if request.method == "GET":
        recipe_id = request.GET.get("recipe_id")
        ingredient_name = request.GET.get("ingredient_name")
        if recipe_id is None and ingredient_name is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_recipe_needs_ingredient")
                recipe_needs_ingredients = cursor.fetchall()
                recipe_needs_ingredients = json.dumps(recipe_needs_ingredients)
                return HttpResponse(recipe_needs_ingredients)
        elif recipe_id is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_recipe_needs_ingredient WHERE ingredient_name = %s", [ingredient_name])
                recipe_needs_ingredients = cursor.fetchall()
                recipe_needs_ingredients = json.dumps(recipe_needs_ingredients)
                return HttpResponse(recipe_needs_ingredients)
        elif ingredient_name is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_recipe_needs_ingredient WHERE recipe_id = %s", [recipe_id])
                recipe_needs_ingredients = cursor.fetchall()
                recipe_needs_ingredients = json.dumps(recipe_needs_ingredients)
                return HttpResponse(recipe_needs_ingredients)
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_recipe_needs_ingredient WHERE recipe_id = %s AND ingredient_name = %s", [recipe_id, ingredient_name])
                recipe_needs_ingredient = cursor.fetchall()
                recipe_needs_ingredient = json.dumps(recipe_needs_ingredient)
                return HttpResponse(recipe_needs_ingredient)
    
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            recipe_id = data["recipe_id"]
            ingredient_name = data["ingredient_name"]
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO api_recipe_needs_ingredient VALUES (%s, %s)", [recipe_id, ingredient_name])
                return HttpResponse("Recipe needs ingredient added")
        except Exception as e:
            return HttpResponse(e)
    
    elif request.method == "DELETE":
        try:
            data = json.loads(request.body)
            recipe_id = request.POST["recipe_id"]
            ingredient_name = request.POST["ingredient_name"]
            
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM api_recipe_needs_ingredient WHERE recipe_id = %s AND ingredient_name = %s", [recipe_id, ingredient_name])
                return HttpResponse("Recipe needs ingredient deleted")
        except Exception as e:
            return HttpResponse(e)
    
    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
            recipe_id = data["recipe_id"]
            ingredient_name = data["ingredient_name"]
            
            with connection.cursor() as cursor:
                cursor.execute("UPDATE api_recipe_needs_ingredient SET recipe_id = %s WHERE ingredient_name = %s", [recipe_id, ingredient_name])
                return HttpResponse("Recipe needs ingredient updated")
        except Exception as e:
            return HttpResponse(e)



### Refrigerator ###
def refrigerator(request):
    if request.method == "GET":
        refrigerator_id = request.GET.get("refrigerator_id")
        user_id = request.GET.get("user_id")
        if refrigerator_id is None and user_id is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_refrigerator")
                refrigerators = cursor.fetchall()
                refrigerators = json.dumps(refrigerators)
                return HttpResponse(refrigerators)
        elif refrigerator_id is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_refrigerator WHERE user_id = %s", [user_id])
                refrigerators = cursor.fetchall()
                refrigerators = json.dumps(refrigerators)
                return HttpResponse(refrigerators)
        elif user_id is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_refrigerator WHERE refrigerator_id = %s", [refrigerator_id])
                refrigerator = cursor.fetchall()
                refrigerator = json.dumps(refrigerator)
                return HttpResponse(refrigerator)
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_refrigerator WHERE refrigerator_id = %s AND user_id = %s", [refrigerator_id, user_id])
                refrigerator = cursor.fetchall()
                refrigerator = json.dumps(refrigerator)
                return HttpResponse(refrigerator)
    
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            user_id = data["user_id"]
            capacity = data["capacity"]
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO api_refrigerator VALUES (%s, %s)", [user_id, capacity])
                return HttpResponse("Refrigerator added")
        except Exception as e:
            return HttpResponse(e)
    
    elif request.method == "DELETE":
        try:
            data = json.loads(request.body)
            refrigerator_id = data["refrigerator_id"]
            
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM api_refrigerator WHERE refrigerator_id = %s", [refrigerator_id])
                return HttpResponse("Refrigerator deleted")
        except Exception as e:
            return HttpResponse(e)
    
    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
            user_id = data["user_id"]
            capacity = data["capacity"]
            
            with connection.cursor() as cursor:
                cursor.execute("UPDATE api_refrigerator SET capacity = %s WHERE user_id = %s", [capacity, user_id])
                return HttpResponse("Refrigerator updated")
        except Exception as e:
            return HttpResponse(e)



### Refrigerator Stores Ingredient ###
def refrigerator_stores_ingredient(request):
    if request.method == "GET":
        refrigerator = request.GET.get("refrigerator")
        ingredient_name = request.GET.get("ingredient_name")
        if refrigerator is None and ingredient_name is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_refrigerator_stores_ingredient")
                refrigerator_stores_ingredients = cursor.fetchall()
                refrigerator_stores_ingredients = json.dumps(refrigerator_stores_ingredients)
                return HttpResponse(refrigerator_stores_ingredients)
        elif refrigerator is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_refrigerator_stores_ingredient WHERE ingredient_name = %s", [ingredient_name])
                refrigerator_stores_ingredients = cursor.fetchall()
                refrigerator_stores_ingredients = json.dumps(refrigerator_stores_ingredients)
                return HttpResponse(refrigerator_stores_ingredients)
        elif ingredient_name is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_refrigerator_stores_ingredient WHERE refrigerator = %s", [refrigerator])
                refrigerator_stores_ingredients = cursor.fetchall()
                refrigerator_stores_ingredients = json.dumps(refrigerator_stores_ingredients)
                return HttpResponse(refrigerator_stores_ingredients)
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_refrigerator_stores_ingredient WHERE refrigerator = %s AND ingredient_name = %s", [refrigerator, ingredient_name])
                refrigerator_stores_ingredient = cursor.fetchall()
                refrigerator_stores_ingredient = json.dumps(refrigerator_stores_ingredient)
                return HttpResponse(refrigerator_stores_ingredient)
    
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            refrigerator = data["refrigerator"]
            ingredient_name = data["ingredient_name"]
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO api_refrigerator_stores_ingredient VALUES (%s, %s)", [refrigerator, ingredient_name])
                return HttpResponse("Refrigerator stores ingredient added")
        except Exception as e:
            return HttpResponse(e)
    
    elif request.method == "DELETE":
        try:
            data = json.loads(request.body)
            refrigerator = request.POST["refrigerator"]
            ingredient_name = request.POST["ingredient_name"]
            
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM api_refrigerator_stores_ingredient WHERE refrigerator = %s AND ingredient_name = %s", [refrigerator, ingredient_name])
                return HttpResponse("Refrigerator stores ingredient deleted")
        except Exception as e:
            return HttpResponse(e)
    
    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
            refrigerator = data["refrigerator"]
            ingredient_name = data["ingredient_name"]
            
            with connection.cursor() as cursor:
                cursor.execute("UPDATE api_refrigerator_stores_ingredient SET refrigerator = %s WHERE ingredient_name = %s", [refrigerator, ingredient_name])
                return HttpResponse("Refrigerator stores ingredient updated")
        except Exception as e:
            return HttpResponse(e)



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
        cursor.execute("DELETE FROM api_review")
        cursor.execute("DELETE FROM api_recipe_needs_ingredient")
        cursor.execute("DELETE FROM api_refrigerator_stores_ingredient")
        cursor.execute("DELETE FROM api_recipe")
        cursor.execute("DELETE FROM api_cuisine")
        cursor.execute("DELETE FROM api_ingredient")
        cursor.execute("DELETE FROM api_refrigerator")
        cursor.execute("DELETE FROM api_user")

        return HttpResponse("All data cleared")
