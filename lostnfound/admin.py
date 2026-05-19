from django.contrib import admin
from .models import Item

# Double check that Item is registered exactly like this
admin.site.register(Item)