from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    age = models.IntegerField()

class Cuisine(models.Model):
    cuisine_name = models.CharField(primary_key=True, max_length=30, null=False)
    method = models.CharField(max_length=30, null=False)
    category = models.CharField(max_length=30, null=False)

class Recipe(models.Model):
    recipe_id = models.IntegerField(primary_key=True, auto_created=True)
    cook_time = models.IntegerField(null=False)
    description = models.CharField(max_length=100, null=False)
    process = models.TextField(null=False)
    cuisine_name = models.ForeignKey(Cuisine, on_delete=models.CASCADE)

class Ingredient(models.Model):
    ingredient_name = models.CharField(primary_key=True, max_length=30, null=False)
    type = models.CharField(max_length=30, null=False)
    calories = models.IntegerField()

class Review(models.Model):
    review_id = models.IntegerField(primary_key=True, auto_created=True)
    content = models.TextField(null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)

class Refrigerator(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False,primary_key=True)
    capacity = models.IntegerField(null=False)

class Recipe_Needs_Ingredient(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, primary_key=True)
    ingredient_name = models.ForeignKey(Ingredient, on_delete=models.CASCADE, primary_key=True)
    
class Refrigerator_Stores_Ingredient(models.Model):
    user_id = models.ForeignKey(Refrigerator, on_delete=models.CASCADE, primary_key=True)
    created_at = models.ForeignKey(Refrigerator, on_delete=models.CASCADE, primary_key=True)
    ingredient_name = models.ForeignKey(Ingredient, on_delete=models.CASCADE, primary_key=True)