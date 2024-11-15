from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('list/', views.members, name='members'),
    path('list/details/<int:id>/', views.details, name='details'),      
    path('testing/', views.testing, name='testing'),      
]
