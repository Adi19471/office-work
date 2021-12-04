from movieApp import views
from django.urls import path

urlpatterns = [
    path('',views.home_Movie,name="home")
]
