from django.shortcuts import render
from empApp.models import Employee
from app2.forms import EmployeeForm
from django.views import View

# Create your views here.
class EmployeeRegisterView(View):
    def get(self,request):
        form=EmployeeForm()
        return render(request,'emp_register.html',{'form':form})