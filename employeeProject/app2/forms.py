from django import forms

class EmployeeForm(forms.Form):
    name=forms.CharField()
    salary=forms.IntegerField()
    designation=forms.CharField()
    email=forms.EmailField()
    phone=forms.IntegerField()



# django forms-normal form,modelform