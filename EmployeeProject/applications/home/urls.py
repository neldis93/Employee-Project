from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('test/',views.TestView.as_view()), # as_view() es un sub metodo que hay que poner cuando utilizamos vistas genericas
    path('list/', views.TestListView.as_view()),
    path('list-test/', views.ToListView.as_view()),
    path('add/', views.TestCreateView.as_view(), name='add'),
    path('summary-foundation', views.SummaryFoundationView.as_view(), name='summary_foundation'),
]