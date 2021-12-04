from django.shortcuts import render,redirect,HttpResponseRedirect

from .models import Complaint,Examsrecord
from .forms import ComplainForm,ExamsrecordForm


# Create your views here.
def home_view(request):
    return render(request,'ONLINE/home.html')


#  create of registration of all fields and diffenrt department
def Register_view(request):
    if request.method=="POST":
        fm = ComplainForm(request.POST)
        if fm.is_valid():
            n1 = fm.cleaned_data['dues_to_the_department']
            n2 = fm.cleaned_data['fees_for_the_hospital_and_bookshop']
            n3 = fm.cleaned_data['charges_for_damage']
            n4 = fm.cleaned_data['returns_all_athletic_gear']
            n5 = fm.cleaned_data['Dues_to_the_student_union']
            n6 = fm.cleaned_data['Male_deal_approal']
            n7 = fm.cleaned_data['obtaining_secutity_chance']

            reg = Complaint(dues_to_the_department=n1,
            fees_for_the_hospital_and_bookshop=n2,
            charges_for_damage=n3,
            returns_all_athletic_gear=n4,
            Dues_to_the_student_union=n5,
            Male_deal_approal=n6,
            obtaining_secutity_chance=n7
            )
            reg.save()
            return redirect('clearence')
    else:
        fm = ComplainForm()           
    context = {'form':fm}
    return render(request,'ONLINE/1activities-register.html',context)



# show data base all 
def clearence_view(request):
    detailes_clearence = Complaint.objects.all()

    context = {'detailes_clearence':detailes_clearence}
    return render(request,'ONLINE/3activities-clearence.html',context)


# update the data base 
def update_Register_view(request,id):
    if request.method=="POST":
        pi = Complaint.objects.get(pk=id)
        fm = ComplainForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('clearence')
    else:
        pi = Complaint.objects.get(pk=id)
        fm = ComplainForm(instance=pi)
        
    context = {'form':fm}
    return render(request,'ONLINE/3.1update-clearence.html',context)


def delete_Register_view(request,id):
    if request.method == "POST":
        pi = Complaint.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')





    return render(request,'ONLINE/4examsrecords.html')

 
def examsrecords_view(request):
    if request.method=="POST":
        fm = ExamsrecordForm(request.POST)
        if fm.is_valid():
          n1 = fm.cleaned_data['name']
          n2 = fm.cleaned_data['passed']
          n3 = fm.cleaned_data['year_of_gap']
          n4 = fm.cleaned_data['message']
          reg = Examsrecord(
              name=n1,passed=n2,year_of_gap=n3,message=n4
          )
          reg.save()
    else:
        fm = ExamsrecordForm()
    examdetailes = Examsrecord.objects.all()           
    context = {'form':fm,'examdetailes':examdetailes}
    return render(request,'ONLINE/4examsrecords.html',context)



def finance_office_view(request):
    return render(request,'ONLINE/defination-1.financeoffice.html')

def library_view(request):
    return render(request, 'ONLINE/defination-2.library.html')

def admision_office_view(request):
    return render(request, 'ONLINE/defination-3.admision_office.html')

def student_affaires_view(request):
    return render(request, 'ONLINE/defination-4.astudent_affaires.html')


def student_security_view(request):
    return render(request, 'ONLINE/defination-5.student_security.html')

def department_coourse_view(request):
    return render(request, 'ONLINE/defination-6.department_coourse.html')
    
    
def faculity_view(request):
    return render(request, 'ONLINE/defination-7.faculity.html')


def alumini_view(request):
    return render(request, 'ONLINE/defination-8.alumini.html')