from django.contrib import admin
from .models import *
admin.autodiscover()

# Register your models here.

admin.site.register(GroceryItem)
admin.site.register(Contact)