from django.shortcuts import render,redirect
from empApp.models import Employee
from app2.forms import EmployeeForm,EmployeeModelForm
from django.views import View
from django.http import HttpResponse

# Create your views here.
class EmployeeRegisterView(View):
    def get(self,request):
        form=EmployeeForm()
        return render(request,'emp_register.html',{'form':form})
    
    def post(self,request):
        form=EmployeeForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data) #{'fname': 'qwerty a', 'salary': 23000, 'designation': 'python developer', 'email': 'qwerty@gmail.com', 'phone': 1234567890}
            Employee.objects.create(**form.cleaned_data)  #(name=,sa)
            return HttpResponse("data added")
        else:
            return HttpResponse("Invalid input")
        

class EmployeeUpdateView(View) :
    def get(self,request,**kwargs):  # {'empid':2}
        emp=Employee.objects.get(id=kwargs.get("empid"))
        form=EmployeeForm(initial={"name":emp.name,"salary":emp.salary,"designation":emp.designation,"email":emp.email,"phone":emp.phone})
        return render(request,'emp_register.html',{'form':form})
    def post(self,request,*args,**kwargs):
        emp=Employee.objects.get(id=kwargs.get("empid"))
        form=EmployeeForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get("name")
            salary=form.cleaned_data.get("salary")
            desig=form.cleaned_data.get("designation")
            email=form.cleaned_data.get("email")
            phone=form.cleaned_data.get("phone")
            emp.name=name
            emp.salary=salary
            emp.designation=desig
            emp.email=email
            emp.phone=phone
            emp.save()
            return redirect("home_view")
            
class ModelRegisterView(View):
    def get(self,request):
        form=EmployeeModelForm()
        return render(request,'emp_register.html',{'form':form})
    def post(self,request):
        form=EmployeeModelForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect("home_view")
class ModelUpdateView(View):
    def get(self,request,**kwargs):
        emp=Employee.objects.get(id=kwargs.get("empid"))
        form=EmployeeModelForm(instance=emp)
        return render(request,'emp_register.html',{'form':form})
    def post(self,request,**kwargs):
        emp=Employee.objects.get(id=kwargs.get("empid"))
        form=EmployeeModelForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect("home_view")

        