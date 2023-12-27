from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from ex1.models import User, Post, Friendship

""" GET /ex2/home/: show home page, the view must contain the posts of other user in Friendship relation (except for deny policy).
GET /ex2/post/{post_id}/: show post with id post_id only if there is a Friendship relation otherwise the page must contain "Access deny".
GET /ex2/user/{username}/: show user page only if there is a Friendship relation otherwise the page must contain "{username} is not your friend"."""

def home(request):
    try:
        user_id = request.session["user_id"]
        if user_id :
           result = User.objects.filter(id=request.session["user_id"])
           username = result[0].username

           friends = Friendship.objects.filter(requester=user_id)
           friends_addressee = [friend.addressee for friend in friends]
           friend_posts = Post.objects.filter(friendship=True)
           _friend_posts = [friend_post for friend_post in friend_posts if friend_post.author in friends_addressee]

           return render(request, 'ex2_templates/home.html', {'posts': _friend_posts, 'username': username})
        
    except KeyError:
        return HttpResponse("home page, not logged, go to login/")
    


def post(request, post_id):
    try:
        p = Post.objects.get(id=post_id)
        user_id = request.session["user_id"]
        if user_id :
           result = User.objects.filter(id=request.session["user_id"])
           username = result[0].username

           friend_post = Post.objects.get(friendship=True, id=post_id)

           friendships = Friendship.objects.filter(requester=user_id)
           friends_addressee = [friend.addressee for friend in friendships]

           if friend_post.author not in friends_addressee:
                return HttpResponse("Post does not exist or you don't have permission to view this post")

    except Exception:
        return HttpResponse("Post does not exist or you don't have permission to view this post")
    return render(request, "ex2_templates/post.html", {"post": p})


def user(request, username):
    try:
        user = User.objects.get(username=username)
        
        user_id = request.session["user_id"]
        if user_id :
           result = User.objects.filter(id=request.session["user_id"])
           friendships = Friendship.objects.get(requester=user_id, addressee=user)

    except Exception:
        return HttpResponse("You don't have permission to view this user")
    return render(request, "ex2_templates/user.html", {"user": user})
    