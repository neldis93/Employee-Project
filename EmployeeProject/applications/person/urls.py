from django.urls import path

from . import views

app_name= 'person_app' # con esto le estoy dando un nombre a todas mis urls para que se pueda acceder a las que tienen el atributo name

urlpatterns = [
    path('', views.StartView.as_view(), name='start'),

    path('list-all-employees/',views.ListAllEmployees.as_view(), name='all_employees'), # as_view() es un sub metodo que hay que poner cuando utilizamos vistas genericas
    path('list-all-department/<shortname>/', views.ListByDepartmentEmployee.as_view(), name='list_employees_department'),
    path('list-employees-admin/', views.ListEmployeesAdmin.as_view(), name='list_employees_admin'),
    path('update-employee/<pk>/',views.EmployeeUpdateView.as_view(), name='update_employee'),
    path('delete-employee/<pk>', views.EmployeeDeleteView.as_view(), name='delete_employee'),
    path('add-employee/',views.EmployeeCreateView.as_view(), name='add_employee'),

    path('list-job-employees/<jobs>/', views.ListJobEmployee.as_view()),
    path('list-kword-employees/',views.ListEmployeeKeyword.as_view()),
    path('list-skill-employee/', views.ListEmployeeSkill.as_view()),
    path('see-employee/<pk>/', views.EmployeeDetailView.as_view(), name='detail_employee'), # pk es un registro que se crea del modelo interno de django, el pk es el id
    path('add-employee/',views.EmployeeCreateView.as_view()),
    path('success/', views.SuccessView.as_view(), name='right'), # con name me permite acceder a toda esta url
    
    

]
