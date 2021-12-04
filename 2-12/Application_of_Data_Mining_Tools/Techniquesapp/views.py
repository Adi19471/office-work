from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request,'Technique/home.html')

def bussines_view(request):
    return render(request,'Technique/bussines_view.html')

def data_understand_view(request):
    return render(request,'Technique/data_understand_view.html')

def data_preparation_view(request):
    return render(request,'Technique/data_preparation_view.html')

def data_modeling_view(request):
    return render(request,'Technique/data_modeling_view.html')


def evalution_view(request):
    return render(request,'Technique/evalution.html')


def deployment_view(request):
    return render(request,'Technique/deployment_view.html')