from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CuisineViewSet, RecipeViewSet, IngredientViewSet, ReviewViewSet, Recipe_Needs_IngredientViewSet, RefrigeratorViewSet, Refrigerator_Stores_IngredientViewSet


from . import views

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cuisines', CuisineViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'recipe_needs_ingredients', Recipe_Needs_IngredientViewSet)
router.register(r'refrigerators', RefrigeratorViewSet)
router.register(r'refrigerator_stores_ingredients', Refrigerator_Stores_IngredientViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
