from django.contrib import admin
from .models import*
# Register your models here.


admin.site.register([Account, Category, SubCategory, Brands, Products])