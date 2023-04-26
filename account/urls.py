from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='signup'),
    path('freelancer/', views.freelancer, name='freelancer'),
    path('client/', views.client, name='client'),
    path("logout", views.logout_request, name= "logout"),
    path("account", views.account, name= "account"),
]
