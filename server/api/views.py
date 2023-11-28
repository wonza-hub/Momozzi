from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .models import User, Cuisine, Recipe, Ingredient, Review, Recipe_Needs_Ingredient, Refrigerator, Refrigerator_Stores_Ingredient
from .serializers import UserSerializer, CuisineSerializer, RecipeSerializer, IngredientSerializer, ReviewSerializer, Recipe_Needs_IngredientSerializer, RefrigeratorSerializer, Refrigerator_Stores_IngredientSerializer


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CuisineViewSet(viewsets.ModelViewSet):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class Recipe_Needs_IngredientViewSet(viewsets.ModelViewSet):
    queryset = Recipe_Needs_Ingredient.objects.all()
    serializer_class = Recipe_Needs_IngredientSerializer

class RefrigeratorViewSet(viewsets.ModelViewSet):
    queryset = Refrigerator.objects.all()
    serializer_class = RefrigeratorSerializer

class Refrigerator_Stores_IngredientViewSet(viewsets.ModelViewSet):
    queryset = Refrigerator_Stores_Ingredient.objects.all()
    serializer_class = Refrigerator_Stores_IngredientSerializer