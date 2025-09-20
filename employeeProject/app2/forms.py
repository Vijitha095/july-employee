from django import forms
from empApp.models import Employee

class EmployeeForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control c1','placeholder':'Name','style':'color:red;background-color:cyan'}))
    salary=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Salary'}))
    designation=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Designation'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    phone=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}))

class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"  # exclude=['phone'] # fields=['name','salary']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'salary':forms.NumberInput(attrs={'class':'form-control','placeholder':'salary'}),
            'designation':forms.TextInput(attrs={'class':'form-control','placeholder':'designation'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'phone'}),
        }