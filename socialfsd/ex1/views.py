from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from .models import User, Post
from .forms import LoginForm, UserForm



def home(request):
    try:
        user_id = request.session["user_id"]
        
        if user_id > 0:
            result = User.objects.filter(id=request.session["user_id"])
            username = result[0].username
            
            result = Post.objects.all()
            
            #return HttpResponse(f'Logged as {username}')
            return render(request, "home.html", {"username": username, "posts": result})
    
    except KeyError:
        return HttpResponse("home page, not logged, go to login/")
    

def user(request, username):
    result = User.objects.filter(username=username)
    if len(result) != 0:
        return HttpResponse(result[0])
    raise Http404(f'No username "{username}" found')

def post(request, post_id):
    try:
        p = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, "post.html", {"post": p})

def login(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            username = form.data["username"]
            password = form.data["password"]
            user_found = User.objects.filter(username=username)
            result = User.objects.filter(username=username, password=password)
            
            if len(result) > 0:
                request.session["user_id"] = result[0].id
                return redirect("home")
            else:
                form.add_error('password', "Wrong password")
             
            
            if len(user_found) <= 0:
                form.add_error('username', "User not found")
            
            
            return render(request, "login.html", {"form": form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})

def logout(request):
    try:
        del request.session["user_id"]
    except KeyError:
        pass
    return HttpResponse("You're logged out.")


from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm
from .models import User

from django.shortcuts import render, redirect
from django.urls import reverse  # Import reverse function
from .forms import UserForm  # Import your UserForm
from .models import User  # Import your User model

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Extract cleaned data from the form
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            bio = form.cleaned_data['bio']
            password = form.cleaned_data['password']

            # Create the user
            user = User.objects.create(username=username, password=password, email=email, bio=bio)
            user.save()

            # Redirect to login page upon successful registration
            return redirect(reverse('login'))  # Redirect to the login URL
        else:
            return render(request, "register.html", {'form': form})
    else:
        form = UserForm()
    
    # Render the form on initial load or when form method is not POST
    return render(request, "register.html", {'form': form})

