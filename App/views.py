from django.shortcuts import render
from .models import Posts

def home(request):
    posts = Posts.objects.all().order_by('-date_creat')
    return render(request, 'home.html', {'posts' : posts})


