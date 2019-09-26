from django.shortcuts import render

# Create your views here
from django.http import HttpResponse

from listings.models import Listing,Category


def index(request):
   
   

   get_list = Listing.objects.order_by("title")

   data = {'title':"Listing Page title",'getListing':get_list}

   
    #listing_data = {'data_listing':"Listing Page title"}

	
   return render(request,'listings/listings_list.html',context=data) 

