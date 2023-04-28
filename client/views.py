from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate , logout
from django.contrib import messages
from .models import AddpostModel
from account.models import User
from django.core.mail import send_mail
from django.conf import settings
from aksconverter_properties_pkg import aksconverter_properties
import boto3
import requests
import json
from datetime import datetime




def AddPost(request):
    # session = boto3.Session( aws_access_key_id='ASIATUYJP7SULTLPXV67', aws_secret_access_key='JEWxfTGhm6c55Gk5SlMyIFhPeMA/qEmTDYpBryjh')
    # s3 = session.resource('s3')
    # my_bucket = s3.Bucket('x22137696-akshay-s3')
    # for objects in my_bucket.objects.filter(Prefix="csv_files/"):
    #     print(objects.key)
    if request.user.is_authenticated and request.user.role == "Client":
        # print(request.user.role)
        current_user = request.user
        if current_user.role == "Client":
             if request.method == 'POST':
                post_title = request.POST.get("post_title")
                post_content = request.POST.get("post_content")
                tags = request.POST.get("tags")
                bidamount = request.POST.get("bidamount")
                tech = request.POST.get('tech')
                user_role = request.POST.get("user_role")
                user_id = 1
                data = {
                    'post_title': post_title,
                    'post_content': post_content,
                    'user_role' : user_role,
                    'tags' : tags,
                    'bidamount' : bidamount,
                    'user_id' : user_id,
                }
                addpost = AddpostModel(post_title=post_title, post_content=post_content, user_role=user_role, user_id=user_id , tags=tags , bidamount=bidamount,tech=tech,)
                subject = post_title + " " + 'New Post Added'
                # print(subject)
                message = post_title
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['akshujoshi41@gmail.com',]
                send_mail( subject, message, email_from, recipient_list )
                test = addpost.save()
                print(addpost)
                messages.success(request, "Post Added")

        return render(request, 'clientpost.html' , {'current_user': current_user})
    else:
       return redirect('index')

def allpost(request):
     if request.user.is_authenticated and request.user.role == "Client":
        Allposts=AddpostModel.objects.filter(user_id=request.user.id).values()
        return render(request, 'viewpost.html' , {'Allposts' : Allposts})

def postdetails(request,id):
    posts=AddpostModel.objects.get(id=id)
    if request.method == 'POST':
        base = request.POST.get("from")
        to = request.POST.get("to")
        amount = request.POST.get("amount")
        con = aksconverter_properties.aksconverter(base , to , amount )
        b = json.loads(con)
        base1 = b['base']
        to1 = b['to']
        amount1 = b['amount']
        converted = b['converted']
        current_rate = b['rate']
        last_update = b['lastUpdate']
        dt_obj = datetime.fromtimestamp(last_update)
        data = {
            'base1': base1,
            'to1': to1,
            'amount1' : amount1,
            'converted' : converted,
            'current_rate' : current_rate,
            'dt_obj' : dt_obj
                    }
        print(data)
        return render(request, 'details.html' , {'posts' : posts , 'data' : data })
    return render(request, 'details.html' , {'posts' : posts })


def postupdate(request,id):
     if request.user.is_authenticated and request.user.role == "Client":
        posts=AddpostModel.objects.filter(user_id=request.user.id).get(id=id)
        if request.method == 'POST':
           posts.post_title = request.POST.get("post_title")
           posts.post_content = request.POST.get("post_content")
           posts.tags = request.POST.get("tags")
           posts.bidamount = request.POST.get("bidamount")
           posts.save()
           messages.success(request, "Post Updated")
        return render(request, 'update.html' , {'posts' : posts})
def postdelete(request,id):
    if request.user.is_authenticated:
       deleteData = AddpostModel.objects.get(id=id)
       deleteData.delete()
       messages.error(request, "Delete")
       return redirect("/allpost")
    return render(request, 'viewpost.html' ,)


