from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    # User endpoints
    path("user/", views.user, name="user"),
    
    # Cuisine endpoints
    path("cuisine/", views.cuisine, name="cuisine"),
    
    # Recipe endpoints
    path("recipe/", views.recipe, name="recipe"),
    path("recipe/search/", views.recipe_search, name="recipe_search"),
    
    # Ingredient endpoints
    path("ingredient/", views.ingredient, name="ingredient"),
    
    # Review endpoints
    path("review/", views.review, name="review"),
    
    # Recipe Needs Ingredient endpoints
    path("recipe_needs_ingredient/", views.recipe_needs_ingredient, name="recipe_needs_ingredient"),
    
    # Refrigerator endpoints
    path("refrigerator/", views.refrigerator, name="refrigerator"),
    
    # Refrigerator Stores Ingredient endpoints
    path("refrigerator_stores_ingredient/", views.refrigerator_stores_ingredient, name="refrigerator_stores_ingredient"),
    
    # Dummy data endpoint
    path("dummy/", views.dummy_add, name="dummy_add"),
    
    # Clear all data endpoint
    path("clear/", views.clear_all, name="clear_all"),
]
