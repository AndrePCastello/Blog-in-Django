from django.shortcuts import render
from .models import Posts

def home(request):
    posts = Posts.objects.all()
    last_post = Posts.objects.order_by('-date_creat').first()
    ##recent_posts = Posts.objects.order_by('-date_creat')
    if last_post:
        previous_post = Posts.objects.filter(date_creat__lt=last_post.date_creat).order_by('-date_creat').first()
    else:
        previous_post = None
    
    return render(request, 'home.html', {'posts': posts, 'last_post': last_post, 'previous_post': previous_post})


