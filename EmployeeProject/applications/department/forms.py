from django import  forms


class NewDepartmentForm(forms.Form):
    name = forms.CharField (max_length=50)
    last_name= forms.CharField(max_length=50)
    department= forms.CharField(max_length=50)
    short_name= forms.CharField(max_length=20)