from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    # User endpoints
    path("user/", views.user, name="user"),
    path("user/<int:user_id>/", views.get_user, name="get_user"),
    
    # Cuisine endpoints
    path("cuisine/", views.cuisine, name="cuisine"),
    path("cuisine/<str:cuisine_name>/", views.get_cuisine, name="get_cuisine"),
    
    # Recipe endpoints
    path("recipe/", views.recipe, name="recipe"),
    path("recipe/<int:recipe_id>/", views.get_recipe, name="get_recipe"),
    
    # Ingredient endpoints
    path("ingredient/", views.ingredient, name="ingredient"),
    path("ingredient/<str:ingredient_name>/", views.get_ingredient, name="get_ingredient"),
    
    # Review endpoints
    path("review/", views.review, name="review"),
    path("review/<int:review_id>/", views.get_review, name="get_review"),
    
    # Recipe Needs Ingredient endpoints
    path("recipe_needs_ingredient/", views.recipe_needs_ingredient, name="recipe_needs_ingredient"),
    path("recipe_needs_ingredient/<int:recipe_id>/<str:ingredient_name>/", views.get_recipe_needs_ingredient, name="get_recipe_needs_ingredient"),
    
    # Refrigerator endpoints
    path("refrigerator/", views.refrigerator, name="refrigerator"),
    path("refrigerator/<int:user_id>/<str:created_at>/", views.get_refrigerator, name="get_refrigerator"),
    
    # Refrigerator Stores Ingredient endpoints
    path("refrigerator_stores_ingredient/", views.refrigerator_stores_ingredient, name="refrigerator_stores_ingredient"),
    path("refrigerator_stores_ingredient/<int:refrigerator>/<str:ingredient_name>/", views.get_refrigerator_stores_ingredient, name="get_refrigerator_stores_ingredient"),
    
    # Dummy data endpoint
    path("dummy/", views.dummy_add, name="dummy_add"),
    
    # Clear all data endpoint
    path("clear/", views.clear_all, name="clear_all"),
]
