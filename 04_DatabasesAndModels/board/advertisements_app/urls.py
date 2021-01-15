from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainView.as_view(), name='Список объявлений'),
    path('fill_db/', views.FillDB.as_view(), name='Добавить 100 записей в БД'),
    path('random/', views.RandomView.as_view(), name='Случайное объявление'),
    path('advertisements/', views.AdsListView.as_view(), name='Список объявлений'),
    path('advertisements/<int:pk>/', views.AdsDetailView.as_view(), name='Список объявлений детали'),
]
