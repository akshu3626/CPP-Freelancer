from django.urls import path
from . import views


urlpatterns = [
    path('addpost', views.AddPost, name= 'addpost'),
    path('allpost', views.allpost, name= 'allpost'),
    path('detail/<int:id>', views.postdetails, name= 'detail'),
    path('update/<int:id>', views.postupdate, name= 'update'),
    path('delete/<int:id>', views.postdelete, name= 'delete'),
]