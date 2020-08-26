from django.urls import path

from . import views

app_name= 'department_app'

urlpatterns = [
    path('new-department/', views.NewDepartmentView.as_view(), name= 'new_department'),
    path('department-list/',views.DepartmentListView.as_view(), name='department_list'),
]
