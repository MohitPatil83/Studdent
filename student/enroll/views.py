from django.shortcuts import render,redirect
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def add_show(request):
     if request.user.is_authenticated:





      if request.method == 'POST':
         
         uname=request.POST['first_name']
         ulast=request.POST['last_name']
         uemail=request.POST['email']
         ucourse=request.POST['course']
         udate_of_birth=request.POST['date_of_birth']
         ugender=request.POST['gender']
         uphone_number=request.POST['phone_number']
         uclass_grade=request.POST['class_grade']
         
         t=Student.objects.create(first_name=uname,last_name=ulast,email=uemail,course=ucourse,date_of_birth=udate_of_birth,gender=ugender,contact_number=uphone_number,class_grade=uclass_grade)
         
         t.save()
         return redirect('/index')
      else:
         
         return render(request,'enroll/addandshow.html')
     else:
         return redirect('/authapp/login')
      
    
     

    
    
def student(request):
     t=Student.objects.all()
     context={}
     context['data']=t
     return render(request,'enroll/index.html',context)

def delete_data(request,rid):
     
          pi=Student.objects.get(pk=rid)
          pi.delete()
          return redirect('/')
def update_date(request,rid):
       if request.method == 'POST':
         
         uname=request.POST['first_name']
         ulast=request.POST['last_name']
         uemail=request.POST['email']
         ucourse=request.POST['course']
         udate_of_birth=request.POST['date_of_birth']
         ugender=request.POST['gender']
         uphone_number=request.POST['phone_number']
         uclass_grade=request.POST['class_grade']
         
         t=Student.objects.filter(id=rid)
         t.update(first_name=uname,last_name=ulast,email=uemail,course=ucourse,date_of_birth=udate_of_birth,gender=ugender,contact_number=uphone_number,class_grade=uclass_grade)
         
         return redirect('/')
       else:
        
        t=Student.objects.get(id=rid)
        context={}
        context['data']=t
        return render(request,'enroll/edit.html',context)
