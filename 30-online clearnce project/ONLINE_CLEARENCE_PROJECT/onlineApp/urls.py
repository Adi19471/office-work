from onlineApp import views
from django.urls import path

urlpatterns = [

    path('',views.home_view,name="Home"),

    # first modules creating part
    path('register/Application',views.Register_view,name="reister"),

    # create clearence
    path('clearence/DATA-detailes',views.clearence_view,name="clearence"),
    path('delete/<int:id>/',views.delete_Register_view,name="delete-clearence"),
    # update clearnece
    path('update/<int:id>/',views.update_Register_view,name="update"),


    path('examsrecords',views.examsrecords_view,name="examsrecord"),


    # deffination role 
    path('finance-detailes/',views.finance_office_view,name="finance"),

    path("library-detailes/", views.library_view, name="library"),
    # library
    path("admision-detailes/", views.admision_office_view, name="admision"),
    # studentaffires
    path("studentaffires-detailes/", views.student_affaires_view, name="studentaffires"),
    # student security
    path("security/", views.student_security_view, name="security"),
    # departments courses all 
    path("department/", views.department_coourse_view, name="department"),
    # faculity 
    path("faculity/detailes", views.faculity_view, name="faculity"),
    # alumini
    path("alumini/detailes", views.alumini_view, name="alumini"),











]
    
