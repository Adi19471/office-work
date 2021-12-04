from . models import Complaint,Examsrecord
from django import forms


class ComplainForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = '__all__'



class ExamsrecordForm(forms.ModelForm):

    class Meta:
        model = Examsrecord
        fields = '__all__'