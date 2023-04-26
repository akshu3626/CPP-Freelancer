from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate , logout
from django.contrib import messages
from .models import AddpostModel
from account.models import User


def AddPost(request):
    if request.user.is_authenticated and request.user.role == "Client":
        # print(request.user.role)
        current_user = request.user
        if current_user.role == "Client":
             if request.method == 'POST':
                post_title = request.POST.get("post_title")
                post_content = request.POST.get("post_content")
                tags = request.POST.get("tags")
                bidamount = request.POST.get("bidamount")
                user_role = request.POST.get("user_role")
                user_id = request.user.id
                data = {
                    'post_title': post_title,
                    'post_content': post_content,
                    'user_role' : user_role,
                    'tags' : tags,
                    'bidamount' : bidamount,
                    'user_id' : user_id,
                }
                addpost = AddpostModel(post_title=post_title, post_content=post_content, user_role=user_role, user_id=request.user.id , tags=tags , bidamount=bidamount)
                addpost.save()
                print(data)
                messages.success(request, "Post Added")
        return render(request, 'clientpost.html' , {'current_user': current_user})
    else:
       return redirect('index')

def allpost(request):
     if request.user.is_authenticated and request.user.role == "Client":
       Allposts=AddpostModel.objects.filter(user_id=request.user.id).values()
       return render(request, 'viewpost.html' , {'Allposts' : Allposts})
        

