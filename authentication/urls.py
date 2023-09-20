from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('create/', views.newUser),
    path('login/', views.logIn),
    path('update/', views.updateUser),
]