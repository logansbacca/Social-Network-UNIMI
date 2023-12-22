from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from ex1.models import User, Post, Friendship


""" GET /ex2/home/: show home page, the view must contain the posts of other user in Friendship relation (except for deny policy).
GET /ex2/post/{post_id}/: show post with id post_id only if there is a Friendship relation otherwise the page must contain "Access deny".
GET /ex2/user/{username}/: show user page only if there is a Friendship relation otherwise the page must contain "{username} is not your friend". """

def home(request):
    try:
        user_id = request.session["user_id"]
        if user_id :
           friends = Friendship.objects.filter(requester=user_id)
           friend_posts = Post.objects.filter(author__in=[friend.addressee for friend in friends])
           return render(request, 'home.html', {'friend_posts': friend_posts})
        
    except KeyError:
        return HttpResponse("home page, not logged, go to login/")
    