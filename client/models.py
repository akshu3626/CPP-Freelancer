from django.db import models
from account.models import User


# Create your models here.

class AddpostModel(models.Model):
    post_title=models.CharField(max_length=100)
    post_content=models.TextField()
    user_role=models.CharField(max_length=100)
    tags=models.CharField(max_length=100 , null=True)
    bidamount=models.CharField(max_length=100 , null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')

    class Meta:
        verbose_name_plural = 'Client Post'
        # Order the blog posts in reverse starting from the latest to the earliest
        ordering = ('-post_title', )

    def __str__(self):
        return self.post_title
    