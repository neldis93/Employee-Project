from django import forms

from .models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ('first_name','last_name','job','department','image','skills',)
        widgets = {'skills':forms.CheckboxSelectMultiple()}
