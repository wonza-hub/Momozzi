from rest_framework import serializers
from .models import User, Cuisine, Recipe, Ingredient, Review, Recipe_Needs_Ingredient, Refrigerator, Refrigerator_Stores_Ingredient

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
        
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class Recipe_Needs_IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe_Needs_Ingredient
        fields = '__all__'

class RefrigeratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refrigerator
        fields = '__all__'

class Refrigerator_Stores_IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refrigerator_Stores_Ingredient
        fields = '__all__'

