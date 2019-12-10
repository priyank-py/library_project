from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_members, name="all_members"),
    path('signup', views.signup, name="signup"),
]
