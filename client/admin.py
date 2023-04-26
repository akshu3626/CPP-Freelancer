from django.contrib import admin
from .models import AddpostModel
 
@admin.register(AddpostModel)
class ClientPost(admin.ModelAdmin):
   pass

