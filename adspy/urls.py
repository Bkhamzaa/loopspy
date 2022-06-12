from django import views
from django.urls import path
from .import views


urlpatterns = [
    path('' ,views.home),
    path('about/' ,views.about),
    path('user/' ,views.users,name="user"),
    path('register/',views.register,name="register"),
    path('login/',views.userlogin,name="login"),
    path('logout/',views.userlogout,name="logout")
]