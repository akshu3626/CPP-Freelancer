from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_client = "Client"
    is_freelancer = "Freelancer"
    
    ROLE = [ (is_client, "Client"),(is_freelancer, "Freelancer"),]
    role = models.CharField(max_length=50,choices=ROLE,default="is_client", null=True )
    