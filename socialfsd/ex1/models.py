from django.db import models
# from django.contrib.auth.models import User

class User(models.Model):
    bio = models.TextField(default='', max_length=200, verbose_name='Bio')
    username = models.CharField(default='', max_length=200, verbose_name='Username')
    password = models.CharField(default='', max_length=200, verbose_name='Password')
    email = models.EmailField(default='', max_length=200, verbose_name='E-mail')
    
    def __str__(self):
        return self.username


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now=True, verbose_name='Date')
    view_counter = models.IntegerField(default=0, verbose_name='View Counter')
    
    def __str__(self):
        return f'{self.author}, {self.text}'
    
class Friendship(models.Model):
    requester = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_requester')
    addressee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_addressee')
        
    def __str__(self):
        return f'{self.requester.username}(requester) <--> {self.addressee.username}'
