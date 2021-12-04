
from django.urls import path
from Techniquesapp import views

urlpatterns = [
    path('',views.home_view,name="home"),
    path('Business/',views.bussines_view,name="businness"),
    path('data/',views.data_understand_view,name="data"),
    path('data-prepparation/',views.data_preparation_view,name="preparation"),
    path('data-modeling/',views.data_modeling_view,name="datamodeling"),
    path('evalution/',views.evalution_view,name="evalution"),
    
    path('deployment-how?process/',views.deployment_view,name="deployment"),



    


]
