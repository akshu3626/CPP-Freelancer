from django.urls import path
from . import views


urlpatterns = [
    path('addpost', views.AddPost, name= 'addpost'),
    path('allpost', views.allpost, name= 'allpost'),
]