from django.urls import path, re_path
from . import views


""" GET /ex2/home/: show home page, the view must contain the posts of other user in Friendship relation (except for deny policy).
GET /ex2/post/{post_id}/: show post with id post_id only if there is a Friendship relation otherwise the page must contain "Access deny".
GET /ex2/user/{username}/: show user page only if there is a Friendship relation otherwise the page must contain "{username} is not your friend". """

app_name = 'ex2'
urlpatterns = [
    path('home/', views.home, name='home'),
    path("user/<str:username>/", views.user, name="user"),
    path("post/<int:post_id>/", views.post, name="post"),
]
