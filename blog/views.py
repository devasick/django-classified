from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
   
   page_title = {'title':"Home Page title"}
	
   return render(request,'index.html',context=page_title)

