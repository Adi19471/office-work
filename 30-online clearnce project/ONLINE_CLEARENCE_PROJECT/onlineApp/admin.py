from django.contrib import admin

# Register your models here.
from .models import Complaint,Examsrecord

admin.site.register(Complaint)
admin.site.register(Examsrecord)
