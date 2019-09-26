#from django.contrib import admin

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Listing,Category

# Register your models here.
class ListingList(admin.ModelAdmin):
	"""docstring for ClassName"""
	list_display = ('title','description','price')
 


admin.site.register(Listing,ListingList)
admin.site.register(Category)

