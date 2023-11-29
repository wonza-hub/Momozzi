from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user/", views.get_all_users, name="get_all_users"),
    path("user/<int:user_id>/", views.get_user, name="get_user"),
    path("user/add/<int:user_id>/<str:first_name>/<str:last_name>/<int:age>/", views.post_user, name="post_user"),
    path("user/delete/<int:user_id>/", views.delete_user, name="delete_user"),
    path("user/update/<int:user_id>/<str:first_name>/<str:last_name>/<int:age>/", views.update_user, name="update_user"),
    
    # Cuisine paths
    path("cuisine/", views.get_all_cuisines, name="get_all_cuisines"),
    path("cuisine/<str:cuisine_name>/", views.get_cuisine, name="get_cuisine"),
    path("cuisine/add/<str:cuisine_name>/<str:method>/<str:category>/", views.post_cuisine, name="post_cuisine"),
    path("cuisine/delete/<str:cuisine_name>/", views.delete_cuisine, name="delete_cuisine"),
    path("cuisine/update/<str:cuisine_name>/<str:method>/<str:category>/", views.update_cuisine, name="update_cuisine"),

    # Recipe paths
    path("recipe/", views.get_all_recipes, name="get_all_recipes"),
    path("recipe/<int:recipe_id>/", views.get_recipe, name="get_recipe"),
    path("recipe/add/<int:recipe_id>/<int:cook_time>/<str:description>/<str:process>/<str:cuisine_name>/", views.post_recipe, name="post_recipe"),
    path("recipe/delete/<int:recipe_id>/", views.delete_recipe, name="delete_recipe"),
    path("recipe/update/<int:recipe_id>/<int:cook_time>/<str:description>/<str:process>/<str:cuisine_name>/", views.update_recipe, name="update_recipe"),

    # Ingredient paths
    path("ingredient/", views.get_all_ingredients, name="get_all_ingredients"),
    path("ingredient/<str:ingredient_name>/", views.get_ingredient, name="get_ingredient"),
    path("ingredient/add/<str:ingredient_name>/<str:type>/<int:calories>/", views.post_ingredient, name="post_ingredient"),
    path("ingredient/delete/<str:ingredient_name>/", views.delete_ingredient, name="delete_ingredient"),
    path("ingredient/update/<str:ingredient_name>/<str:type>/<int:calories>/", views.update_ingredient, name="update_ingredient"),

    # Review paths
    path("review/", views.get_all_reviews, name="get_all_reviews"),
    path("review/<int:review_id>/", views.get_review, name="get_review"),
    path("review/add/<int:review_id>/<str:content>/<int:user_id>/<int:recipe_id>/", views.post_review, name="post_review"),
    path("review/delete/<int:review_id>/", views.delete_review, name="delete_review"),
    path("review/update/<int:review_id>/<str:content>/<int:user_id>/<int:recipe_id>/", views.update_review, name="update_review"),

    # Recipe_Needs_Ingredient paths
    path("recipe_needs_ingredient/", views.get_all_recipe_needs_ingredients, name="get_all_recipe_needs_ingredients"),
    path("recipe_needs_ingredient/<int:recipe_id>/<str:ingredient_name>/", views.get_recipe_needs_ingredient, name="get_recipe_needs_ingredient"),
    path("recipe_needs_ingredient/add/<int:recipe_id>/<str:ingredient_name>/", views.post_recipe_needs_ingredient, name="post_recipe_needs_ingredient"),
    path("recipe_needs_ingredient/delete/<int:recipe_id>/<str:ingredient_name>/", views.delete_recipe_needs_ingredient, name="delete_recipe_needs_ingredient"),
    path("recipe_needs_ingredient/update/<int:recipe_id>/<str:ingredient_name>/", views.update_recipe_needs_ingredient, name="update_recipe_needs_ingredient"),

    # Refrigerator paths
    path("refrigerator/", views.get_all_refrigerators, name="get_all_refrigerators"),
    path("refrigerator/<int:user_id>/<str:created_at>/", views.get_refrigerator, name="get_refrigerator"),
    path("refrigerator/add/<int:user_id>/<str:created_at>/<int:capacity>/", views.post_refrigerator, name="post_refrigerator"),
    path("refrigerator/delete/<int:user_id>/<str:created_at>/", views.delete_refrigerator, name="delete_refrigerator"),
    path("refrigerator/update/<int:user_id>/<str:created_at>/<int:capacity>/", views.update_refrigerator, name="update_refrigerator"),

    # Refrigerator_Stores_Ingredient paths
    path("refrigerator_stores_ingredient/", views.get_all_refrigerator_stores_ingredients, name="get_all_refrigerator_stores_ingredients"),
    path("refrigerator_stores_ingredient/<int:refrigerator>/<str:ingredient_name>/", views.get_refrigerator_stores_ingredient, name="get_refrigerator_stores_ingredient"),
    path("refrigerator_stores_ingredient/add/<int:refrigerator>/<str:ingredient_name>/", views.post_refrigerator_stores_ingredient, name="post_refrigerator_stores_ingredient"),
    path("refrigerator_stores_ingredient/delete/<int:refrigerator>/<str:ingredient_name>/", views.delete_refrigerator_stores_ingredient, name="delete_refrigerator_stores_ingredient"),
    path("refrigerator_stores_ingredient/update/<int:refrigerator>/<str:ingredient_name>/", views.update_refrigerator_stores_ingredient, name="update_refrigerator_stores_ingredient"),

    # Dummy paths
    path("dummy/", views.dummy_add, name="dummy_add"),
    
    # Clear paths
    path("clear/", views.clear_all, name="clear_all"),
]
