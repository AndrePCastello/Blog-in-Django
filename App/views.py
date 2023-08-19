from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all().order_by('-date_creat')
    return render(request, 'home.html', {'posts' : posts})


def posts_for_date(request, date):
    posts = Post.objects.filter(date_creat__date=date).order_by('-date_creat')
    return render (request, 'posts-for-date.html', {'posts' : posts, 'data' : date})


def details_post(request, id_post):
    post = Post.objects.get(pk=id_post)
    return render (request, 'details-for-post.html', {'post' : post})

