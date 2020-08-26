from django.shortcuts import render
from django.urls import reverse_lazy 
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView

# models
from .models import Employee
# forms
from .forms import EmployeeForm

""" Desarrollo del proyecto """

class StartView(TemplateView):
    """ vista que carga la pagina de inicio """
    template_name= 'start.html'

"""ListView"""
# Practica con ListView
# 1.- Lista todos los empleados de la empresa
# 2.- Listar a todos los empleados que pertenencen a un area de la empresa 
# 3.- Listar empleados por trabajo
# 4.- Listar empleados por palabra clave
# 5.- Listar habilidades de un empleado
#---------------------------------------------------------------


#1.
class ListAllEmployees(ListView):
    template_name= 'person/list_all.html'
    #model= Employee
    paginate_by= 5 # Paginacion en ListView, nos mostrara los cuatro primeros empleados
    ordering='first_name'
    context_object_name= 'list_all_employees' # este parametro es el que le pasamos al html para llamar a la clase ListAllEmplooyes

    # con get_queryset no hace falta pasar el model= Employee
    def get_queryset(self):
        key_word= self.request.GET.get('keyword','') # con esto intercepto con GET el id y name= keyword en mi list_keyword.html 
        list_keyword= Employee.objects.filter(first_name__icontains= key_word) # incontains encuentra cadenas ej: jo= Jorge
        return list_keyword


# Administrar
class ListEmployeesAdmin(ListView):
    template_name= 'person/list_employee.html'
    model= Employee 
    paginate_by= 10 
    ordering='first_name'
    context_object_name= 'list_all_employees'


#2.
class ListByDepartmentEmployee(ListView):
    template_name= 'person/list_all_department.html'
    context_object_name= 'list_department'  # cuando no lo utilizamos pondremos en el html object_list

    def get_queryset(self):
        department_employee= self.kwargs['shortname'] # el shortname es el que pongo en la urls.py
        list_empl= Employee.objects.filter(department__short_name= department_employee) # filtro por URL
        return list_empl


#3.
class ListJobEmployee(ListView):
    template_name= 'person/list_job.html'
    #context_object_name='job'

    def get_queryset(self):
        job_url= self.kwargs['jobs']
        list_job= Employee.objects.filter(job= job_url)
        return list_job

#4.
class ListEmployeeKeyword(ListView):
    template_name='person/list_keyword.html'
    context_object_name= 'keyword'
    
    def get_queryset(self):
        key_word= self.request.GET.get('keyword','') # con esto intercepto con GET el id y name= keyword en mi list_keyword.html 
        list_keyword= Employee.objects.filter(first_name= key_word)
        #print('============ ', list_keyword)
        return list_keyword

#5.
class ListEmployeeSkill(ListView):
    template_name= 'person/list_skills.html'
    context_object_name= 'skill'

    def get_queryset(self):
        employee= Employee.objects.get(id=1)
        return employee.skills.all()



""" DetailView """

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'person/detail_employee.html'  
        
    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        context['title']= 'Employee of the Month'
        return context
        
""" CreateView """


class SuccessView(TemplateView):
    template_name = "person/success.html"

# este metodo trabaja con un formulario en html y los datos van a la base de datos, es decir es la vista que hace el registro
class EmployeeCreateView(CreateView):
    template_name = "person/add.html"
    model = Employee
    #fields= ('__all__') # con esto le estamos indicando que nos traiga todo los atributos de la class Employee de models.py
    #fields= ['first_name', 'last_name', 'job', 'department', 'skills','image']
    form_class= EmployeeForm
    success_url= reverse_lazy('person_app:list_employees_admin')
    
    def form_valid(self, form):
        #logica del proceso
        employee= form.save(commit= False) # hacemos un guardado del proceso
        employee.full_name= employee.first_name + ' ' + employee.last_name
        employee.save()
        #El super se utiliza para sobreescribir la funcion
        return super(EmployeeCreateView,self).form_valid(form) 


""" UpdateView """


class EmployeeUpdateView(UpdateView):
    template_name = "person/update.html"
    model = Employee
    fields= ['first_name', 'last_name', 'job', 'department', 'skills']
    success_url= reverse_lazy('person_app:list_employees_admin')


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('************************************')
        print('************ METHOD POST ***********')
        print('************************************')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)


    def form_valid(self, form):
       #logica del proceso
        print('************************************')
        print('******** METHOD FORM VALID *********')
        print('************************************')
        #El super se utiliza para sobreescribir la funcion
        return super(EmployeeUpdateView,self).form_valid(form)


""" DeleteView """


class EmployeeDeleteView(DeleteView):
    template_name = "person/delete.html"
    model = Employee
    success_url= reverse_lazy('person_app:list_employees_admin')
    

    
