from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/for-date/<str:date>', views.posts_for_date, name='posts_for_date'),
    path('details_post/ <int:id_post>', views.details_post, name='details_post')
]

