from django.db import models

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    age = models.IntegerField()

class Cuisine(models.Model):
    cuisine_id = models.BigAutoField(primary_key=True)
    cuisine_name = models.CharField(max_length=30, unique=True)
    method = models.CharField(max_length=30)
    category = models.CharField(max_length=30)

class Recipe(models.Model):
    recipe_id = models.BigAutoField(primary_key=True)
    cook_time = models.IntegerField()
    description = models.TextField()
    process = models.TextField()
    cuisine_name = models.ForeignKey(Cuisine, on_delete=models.CASCADE, db_column='cuisine_name', to_field='cuisine_name')

class Ingredient(models.Model):
    ingredient_name = models.CharField(primary_key=True, max_length=30)
    type = models.CharField(max_length=30)
    calories = models.IntegerField()

class Review(models.Model):
    review_id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, db_column='recipe_id')

class Recipe_Needs_Ingredient(models.Model):
    id = models.BigAutoField(primary_key=True)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, db_column='recipe_id')
    ingredient_name = models.ForeignKey(Ingredient, on_delete=models.CASCADE, db_column='ingredient_name')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['recipe_id', 'ingredient_name'], name='unique_recipe_ingredient')
        ]

class Refrigerator(models.Model):
    refrigerator_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    capacity = models.IntegerField()
    
    class Meta:        
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'created_at'], name='unique_refrigerator')
        ]

class Refrigerator_Stores_Ingredient(models.Model):
    id = models.BigAutoField(primary_key=True)
    refrigerator_id = models.ForeignKey(Refrigerator, on_delete=models.CASCADE, db_column='refrigerator_id')
    ingredient_name = models.ForeignKey(Ingredient, on_delete=models.CASCADE, db_column='ingredient_name')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['refrigerator_id', 'ingredient_name'], name='unique_refrigerator_ingredient')
        ]