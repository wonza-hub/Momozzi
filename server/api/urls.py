from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    # User endpoints
    path("user/", views.user, name="user"),
    path("user/login/", views.user_login, name="user_login"),
    
    # Cuisine endpoints
    path("cuisine/", views.cuisine, name="cuisine"),
    
    # Recipe endpoints
    path("recipe/", views.recipe, name="recipe"),
    path("recipe/keyword/", views.recipe_keyword, name="recipe_keyword"),
    path("recipe/filter/", views.recipe_filter, name="recipe_filter"),
    path("recipe/top/", views.recipe_top, name="recipe_top"),
    path("recipe/fast/", views.recipe_fast, name="recipe_fast"),
    
    # Ingredient endpoints
    path("ingredient/", views.ingredient, name="ingredient"),
    
    # Review endpoints
    path("review/", views.review, name="review"),
    
    # Recipe Needs Ingredient endpoints
    path("recipe_needs_ingredient/", views.recipe_needs_ingredient, name="recipe_needs_ingredient"),
    
    # Refrigerator endpoints
    path("refrigerator/", views.refrigerator, name="refrigerator"),
    path("refrigerator/recommend/", views.recommend_recipe_by_refrigerator, name="recommend_recipe_by_refrigerator"),
    
    # Refrigerator Stores Ingredient endpoints
    path("refrigerator_stores_ingredient/", views.refrigerator_stores_ingredient, name="refrigerator_stores_ingredient"),
    
    # User Likes Cuisine endpoints
    path("user_likes_cuisine/", views.user_likes_cuisine, name="user_likes_cuisine"),
    
    # Dummy data endpoint
    path("dummy/", views.dummy_add, name="dummy_add"),
    
    # Clear all data endpoint
    path("clear/", views.clear_all, name="clear_all"),
]
