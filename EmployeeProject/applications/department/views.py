from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView

from .forms import NewDepartmentForm
from applications.person.models import Employee
from .models import Department



class DepartmentListView(ListView):
    model = Department
    template_name = 'department/list.html'
    context_object_name= 'departments'

class NewDepartmentView(FormView):
    template_name= 'department/new_department.html'
    form_class= NewDepartmentForm
    success_url= '/'

    def form_valid(self,form):
        # Instanacia con clase Department 
        depa= Department(name= form.cleaned_data['department'],short_name=form.cleaned_data['short_name'])
        depa.save()

        names= form.cleaned_data['name']
        last_names= form.cleaned_data['last_name']
        Employee.objects.create(first_name= names,last_name=last_names, job='1', department= depa) # el 1 indica 

        return super(NewDepartmentView,self).form_valid(form)
