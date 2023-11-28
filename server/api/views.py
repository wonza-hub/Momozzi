from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
import json


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def get_all_users(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM api_user")
        users = cursor.fetchall()
        return HttpResponse(users)
    
def get_user(request, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM api_user WHERE user_id = %s", [user_id])
        user = cursor.fetchone()
        return HttpResponse(user)

def post_user(request, user_id, first_name, last_name, age):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO api_user VALUES (%s, %s, %s, %s)", [user_id, first_name, last_name, age])
        return HttpResponse("User added")