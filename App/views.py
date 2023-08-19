from django.shortcuts import render
from .models import Posts

def home(request):
    posts = Posts.objects.all().order_by('-date_creat')
    return render(request, 'home.html', {'posts' : posts})


def posts_for_date(request, date):
    posts = Posts.objects.filter(date_creat__date=date).order_by('-date_creat')
    return render (request, 'posts-for-date.html', {'posts' : posts, 'data' : date})
