from django.urls import path
from . import views

urlpatterns = [
    path('', views.test,name="test"),
    path('login/', views.loginPage, name="loginc"),
    path('logout/', views.logoutUser, name="logoutc"),
    path('register/', views.registerPage, name="registerc"),
    path('compte/', views.compte, name="comptecan"),
    path('candida/', views.candidature, name="candidat"),
    path('delete_candidature/', views.delete_candidature, name='delete_candidature'),
    path('view_score/<int:candidature_id>/', views.view_score, name='view_score'),
    path('profile_form/', views.profile_form, name='profile_form'),
    path('settings/', views.profile_details, name='settingscan'),

]