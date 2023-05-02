![](socialFSD.png)


_Webapp del corso di FSD (Bruschi, Rusconi, Zoia) @ Unimi 2023_


# Lab 1
* `mkdir social-fsd`
* `cd social-fsd`
* `python3 -m venv .venv`
* `source .venv/bin/activate`
* `python3 -m pip install -r requirements.txt`
* `mkdir socialfsd`
* `cd socialfsd`
* `django-admin startproject socialfsd .`
* `cd socialfsd`
* `python manage.py migrate`
* `python manage.py runserver`
* Check that everything is good at http://localhost:8000/

**Task 1**: Create your own Django app with a minimal UI following this tutorial: https://docs.djangoproject.com/en/1.8/intro/tutorial01/.

**Task 2**: Create a model to handle users and posts. Users are entities that have a username, bio, email, password and a list of posts. Posts are entities that have content (only text), author, date, and view counter.

**Task 3**: Create a login page to manage sessions, allowing only logged-in accounts to see user posts. Every logged-in user can see all other users' posts (meaning that every user is in a friend relationship with everyone else).

Add some records using the admin page to test the functionalities.

## Endpoints
* GET `/ex1/user/{username}/`: show user page, the view must contain the username of the user and its bio.
* GET `/ex1/post/{post_id}/`: show post with id `post_id`, the view must contain the text of the post.
* POST `/ex1/login/` {username:str, password:str}: if the username was not found the webapp should add "User not found" inside the page, if the password is wrong the webapp should add "Wrong password" inside the page; both options are possible.

For detailed webapp behavior you can check `ex1/tests/tests.py`, tests are triggered by a push on master branch.