from django.shortcuts import get_object_or_404, render
from .models import Posts

def home(request):
    posts = Posts.objects.all().order_by('-date_creat')
    return render(request, 'home.html', {'posts' : posts})


def posts_for_date(request, date):
    posts = Posts.objects.filter(date_creat__date=date).order_by('-date_creat')
    return render (request, 'posts-for-date.html', {'posts' : posts, 'data' : date})


def details_post(request, id_post):
    post = Posts.objects.get(pk=id_post)
    return render (request, 'details-for-post.html', {'post' : post})