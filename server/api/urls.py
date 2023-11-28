from django.urls import path, include
from . import tests
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("users/", views.get_all_users, name="get_all_users"),
    
    
    path("users_dummy/", tests.dummy_user_add, name="dummy_user_add"),
]
