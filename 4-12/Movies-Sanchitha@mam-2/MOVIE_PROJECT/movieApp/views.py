from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render,HttpResponse


# Create your views here.

def home_Movie(request):
    # return render(request,'M/1home_Movie.html')
    return HttpResponse("Hello")