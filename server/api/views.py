from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
import json
import pymysql.cursors
from django.views.decorators.csrf import csrf_exempt
from .dummy import dummy_user_add, dummy_cuisine_add, dummy_recipe_add, dummy_ingredient_add, dummy_review_add, dummy_recipe_needs_ingredient_add, dummy_refrigerator_add, dummy_refrigerator_stores_ingredient_add

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


### User ###
@csrf_exempt
def user(request):    
    if request.method == "GET":
        user_id = request.GET.get("user_id")
        email = request.GET.get("email")
        if user_id is None and email is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_user")
                users = dictfetchall(cursor)
                return JsonResponse(users, safe=False)
            
        elif user_id is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_user WHERE email = %s", [email])
                users = dictfetchall(cursor)
                return JsonResponse(users, safe=False)
            
        elif email is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_user WHERE user_id = %s", [user_id])
                users = dictfetchall(cursor)
                return JsonResponse(users, safe=False)
            
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_user WHERE user_id = %s AND email = %s", [user_id, email])
                users = dictfetchall(cursor)
                return JsonResponse(users, safe=False)
    
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data["email"]
            first_name = data["first_name"]
            last_name = data["last_name"]
            password = data["password"]
            age = data["age"]
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO api_user (email, first_name, last_name, password, age) VALUES (%s, %s, %s, %s, %s)", [email, first_name, last_name, password, age])
                users = dictfetchall(cursor)
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
            email = data["email"]
            first_name = data["first_name"]
            last_name = data["last_name"]
            password = data["password"]
            age = data["age"]
            
            with connection.cursor() as cursor:
                cursor.execute("UPDATE api_user SET email = %s, first_name = %s, last_name = %s, password = %s, age = %s WHERE user_id = %s", [email, first_name, last_name, password, age, user_id])
                users = dictfetchall(cursor)
                return JsonResponse(users, safe=False)
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
                user = dictfetchall(cursor)
                return JsonResponse(user, safe=False)
        except Exception as e:
            return HttpResponse(e)
        

### Cuisine ###
def cuisine(request):
    if request.method == "GET":
        cuisine_name = request.GET.get("cuisine_name")
        if cuisine_name is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_cuisine")
                cuisines = dictfetchall(cursor)
                return JsonResponse(cuisines, safe=False)
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_cuisine WHERE cuisine_name = %s", [cuisine_name])
                cuisines = dictfetchall(cursor)
                return JsonResponse(cuisines, safe=False)
    
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            cuisine_name = data["cuisine_name"]
            method = data["method"]
            category = data["category"]
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO api_cuisine VALUES (%s, %s, %s)", [cuisine_name, method, category])
                cuisines = dictfetchall(cursor)
                return JsonResponse(cuisines, safe=False)
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
                cuisines = dictfetchall(cursor)
                return JsonResponse(cuisines, safe=False)
        except Exception as e:
            return HttpResponse(e)

### Recipe ###
def recipe(request):
    if request.method == "GET":
        recipe_id = request.GET.get("recipe_id")
        cuisine_name = request.GET.get("cuisine_name")
        if recipe_id is None and cuisine_name is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_recipe")
                recipes = dictfetchall(cursor)
                return JsonResponse(recipes, safe=False)
        elif recipe_id is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_recipe WHERE cuisine_name = %s", [cuisine_name])
                recipes = dictfetchall(cursor)
                return JsonResponse(recipes, safe=False)
        elif cuisine_name is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_recipe WHERE recipe_id = %s", [recipe_id])
                recipes = dictfetchall(cursor)
                return JsonResponse(recipes, safe=False)
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_recipe WHERE recipe_id = %s AND cuisine_name = %s", [recipe_id, cuisine_name])
                recipes = dictfetchall(cursor)
                return JsonResponse(recipes, safe=False)
    
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            cook_time = data["cook_time"]
            description = data["description"]
            process = data["process"]
            cuisine_name = data["cuisine_name"]
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO api_recipe (cook_time, description, process, cuisine_name) VALUES (%s, %s, %s, %s)", [cook_time, description, process, cuisine_name])
                recipes = dictfetchall(cursor)
                return JsonResponse(recipes, safe=False)
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
            cook_time = data["cook_time"]
            description = data["description"]
            process = data["process"]
            cuisine_name = data["cuisine_name"]
            
            with connection.cursor() as cursor:
                cursor.execute("UPDATE api_recipe SET cook_time = %s, description = %s, process = %s WHERE cuisine_name = %s", [cook_time, description, process, cuisine_name])
                recipes = dictfetchall(cursor)
                return JsonResponse(recipes, safe=False)
        except Exception as e:
            return HttpResponse(e)

def recipe_keyword(request):
    if request.method == "GET":
        keyword = request.GET.get("keyword")
        if keyword is not None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_recipe WHERE description LIKE %s", ["%" + keyword + "%"])
                recipes = dictfetchall(cursor)
                return JsonResponse(recipes, safe=False)
        
        else:
            return HttpResponse("No search criteria")

def recipe_filter(request):
    if request.method == "GET":
        method = request.GET.get("method")
        category = request.GET.get("category")
        ingredient_name = request.GET.get("ingredient")

        query = """
            SELECT DISTINCT r.* FROM api_recipe r
            INNER JOIN api_cuisine c ON r.cuisine_name = c.cuisine_name
            INNER JOIN api_recipe_needs_ingredient rni ON r.recipe_id = rni.recipe_id
            INNER JOIN api_ingredient i ON rni.ingredient_name = i.ingredient_name
        """

        conditions = []
        params = []

        if method:
            conditions.append("c.method = %s")
            params.append(method)
        if category:
            conditions.append("c.category = %s")
            params.append(category)
        if ingredient_name:
            conditions.append("i.ingredient_name = %s")
            params.append(ingredient_name)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        with connection.cursor() as cursor:
            cursor.execute(query, params)
            recipes = dictfetchall(cursor)
            return JsonResponse(recipes, safe=False)
        
def recommend_recipe_by_refrigerator(request):
    if request.method == "GET":
        refrigerator_id = request.GET.get("refrigerator")
        if refrigerator_id is not None:
            with connection.cursor() as cursor:     # todo : make this view
                cursor.execute("""
                    SELECT r.* 
                    FROM api_recipe r
                    WHERE NOT EXISTS (
                        SELECT 1
                        FROM api_recipe_needs_ingredient rni
                        WHERE rni.recipe_id = r.recipe_id
                        AND rni.ingredient_name NOT IN (
                            SELECT rsi.ingredient_name
                            FROM api_refrigerator_stores_ingredient rsi
                            WHERE rsi.refrigerator_id = %s
                        )
                    )
                """, [refrigerator_id])
                recipes = dictfetchall(cursor)
                return JsonResponse(recipes, safe=False)
        else:
            return JsonResponse([], safe=False)
        


### Ingredient ###
def ingredient(request):
    if request.method == "GET":
        ingredient_name = request.GET.get("ingredient_name")
        if ingredient_name is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_ingredient")
                ingredients = dictfetchall(cursor)
                return JsonResponse(ingredients, safe=False)
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_ingredient WHERE ingredient_name = %s", [ingredient_name])
                ingredients = dictfetchall(cursor)
                return JsonResponse(ingredients, safe=False)
    
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
@csrf_exempt
def review(request):
    if request.method == "GET":
        review_id = request.GET.get("review_id")
        recipe_id = request.GET.get("recipe_id")
        
        if review_id is None and recipe_id is None:
            with connection.cursor() as cursor:
                cursor.execute(cursor.execute("""
                    SELECT r.*, u.first_name, u.last_name 
                    FROM api_review r
                    JOIN api_user u ON r.user_id = u.user_id
                """))
                reviews = dictfetchall(cursor)
                return JsonResponse(reviews, safe=False)
            
        elif review_id is None:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT r.*, u.first_name, u.last_name
                    FROM api_review r
                    JOIN api_user u ON r.user_id = u.user_id
                    WHERE recipe_id = %s
                """, [recipe_id])
                reviews = dictfetchall(cursor)
                return JsonResponse(reviews, safe=False)
            
        elif recipe_id is None:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT r.*, u.first_name, u.last_name
                    FROM api_review r
                    JOIN api_user u ON r.user_id = u.user_id
                    WHERE review_id = %s
                """, [review_id])
                reviews = dictfetchall(cursor)
                return JsonResponse(reviews, safe=False)
            
        else:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT r.*, u.first_name, u.last_name
                    FROM api_review r
                    JOIN api_user u ON r.user_id = u.user_id
                    WHERE review_id = %s AND recipe_id = %s
                """, [review_id, recipe_id])
                reviews = dictfetchall(cursor)
                return JsonResponse(reviews, safe=False)
    
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            content = data["content"]
            user_id = data["user_id"]
            recipe_id = data["recipe_id"]
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO api_review (content, user_id, recipe_id) VALUES (%s, %s, %s)", [content, user_id, recipe_id])
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
                recipe_needs_ingredients = dictfetchall(cursor)
                return JsonResponse(recipe_needs_ingredients, safe=False)
        elif recipe_id is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_recipe_needs_ingredient WHERE ingredient_name = %s", [ingredient_name])
                recipe_needs_ingredients = dictfetchall(cursor)
                return JsonResponse(recipe_needs_ingredients, safe=False)
        elif ingredient_name is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_recipe_needs_ingredient WHERE recipe_id = %s", [recipe_id])
                recipe_needs_ingredients = dictfetchall(cursor)
                return JsonResponse(recipe_needs_ingredients, safe=False)
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_recipe_needs_ingredient WHERE recipe_id = %s AND ingredient_name = %s", [recipe_id, ingredient_name])
                recipe_needs_ingredients = dictfetchall(cursor)
                return JsonResponse(recipe_needs_ingredients, safe=False)
    
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
        refrigerator_id = request.GET.get("refrigerator")
        user_id = request.GET.get("user_id")
        if refrigerator_id is None and user_id is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_refrigerator")
                refrigerators = dictfetchall(cursor)
                return JsonResponse(refrigerators, safe=False)
        elif refrigerator_id is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_refrigerator WHERE user_id = %s", [user_id])
                refrigerators = dictfetchall(cursor)
                return JsonResponse(refrigerators, safe=False)
        elif user_id is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_refrigerator WHERE refrigerator_id = %s", [refrigerator_id])
                refrigerators = dictfetchall(cursor)
                return JsonResponse(refrigerators, safe=False)
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM api_refrigerator WHERE refrigerator_id = %s AND user_id = %s", [refrigerator_id, user_id])
                refrigerators = dictfetchall(cursor)
                return JsonResponse(refrigerators, safe=False)
    
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
            refrigerator_id = data["refrigerator"]
            
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
                cursor.execute("""
                    SELECT *
                    FROM api_refrigerator_stores_ingredient rsi
                    JOIN api_ingredient i ON rsi.ingredient_name = i.ingredient_name
                    """) 
                refrigerator_stores_ingredients = dictfetchall(cursor)
                return JsonResponse(refrigerator_stores_ingredients, safe=False)
        elif refrigerator is None:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT *
                    FROM api_refrigerator_stores_ingredient rsi
                    JOIN api_ingredient i ON rsi.ingredient_name = i.ingredient_name
                    WHERE i.ingredient_name = %s
                    """, [ingredient_name]) 
                refrigerator_stores_ingredients = dictfetchall(cursor)
                return JsonResponse(refrigerator_stores_ingredients, safe=False)
        elif ingredient_name is None:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT *
                    FROM api_refrigerator_stores_ingredient rsi
                    JOIN api_ingredient i ON rsi.ingredient_name = i.ingredient_name
                    WHERE rsi.refrigerator_id = %s
                    """, [refrigerator])
                refrigerator_stores_ingredients = dictfetchall(cursor)
                return JsonResponse(refrigerator_stores_ingredients, safe=False)
        else:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT *
                    FROM api_refrigerator_stores_ingredient rsi
                    JOIN api_ingredient i ON rsi.ingredient_name = i.ingredient_name
                    WHERE rsi.refrigerator_id = %s AND i.ingredient_name = %s
                    """, [refrigerator, ingredient_name])
                refrigerator_stores_ingredients = dictfetchall(cursor)
                return JsonResponse(refrigerator_stores_ingredients, safe=False)
    
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
