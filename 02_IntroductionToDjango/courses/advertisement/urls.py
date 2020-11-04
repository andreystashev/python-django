
from django.urls import path
from .import views

urlpatterns = [
    path("module1", views.m1, name='1 modul'),
    path("module2", views.m2, name='2 modul'),
    path("module3", views.m3, name='3 modul'),
    path("module4", views.m4, name='4 modul'),
    path("module5", views.m5, name='5 modul'),
    path("", views.main, name='main')

]