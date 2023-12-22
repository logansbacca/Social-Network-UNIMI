from django.urls import path, re_path
from . import views


urlpatterns = [
    # ex: /intro/home/
    path("home/", views.home, name="home"),
    # ex: /intro/login/
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    # ex: /intro/matteo/
    path("user/<str:username>/", views.user, name="user"),
    # ex: /intro/5652/
    path("post/<int:post_id>/", views.post, name="post"),
]



