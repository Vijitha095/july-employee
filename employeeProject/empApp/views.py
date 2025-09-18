from django.shortcuts import render,redirect
from django.views import View
from empApp.models import Employee

# Create your views here.
class HomeView(View):
    def get(self,request):
        employees=Employee.objects.all()
        return render(request,'index.html',{"employees":employees})
    
class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        name=request.POST.get("name")
        salary=request.POST.get("salary")
        desig=request.POST.get("desig")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        Employee.objects.create(name=name,salary=salary,designation=desig,email=email,phone=phone)
        return redirect("home_view")
    
class DeleteView(View):
    def get(self,request,*args,**kwargs):
        Employee.objects.get(id=kwargs.get("id")).delete()
        return redirect("home_view")
    
class UpdateView(View):
    def get(self,request,*args,**kwargs):
        employee=Employee.objects.get(id=kwargs.get("id"))
        return render(request,"register.html",{'employee':employee})
    def post(self,request,*args,**kwargs):
        employee=Employee.objects.get(id=kwargs.get("id"))
        name=request.POST.get("name")
        salary=request.POST.get("salary")
        desig=request.POST.get("desig")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        employee.name=name
        employee.salary=salary
        employee.designation=desig
        employee.email=email
        employee.phone=phone
        employee.save()
        return redirect("home_view")
    
        