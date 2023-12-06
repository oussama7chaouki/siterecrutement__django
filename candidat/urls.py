from django.urls import path
from . import views

urlpatterns = [
    path('', views.test,name="test"),
    path('login/', views.loginPage, name="loginc"),
    path('logout/', views.logoutUser, name="logoutc"),
    path('register/', views.registerPage, name="registerc"),
    path('compte/', views.compte, name="comptecan"),


]