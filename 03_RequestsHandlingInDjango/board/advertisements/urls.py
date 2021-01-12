from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage.as_view()),
    path('contacts/', views.Contacts.as_view()),
    path('about/', views.About.as_view()),
    path('regions/', views.Regions.as_view()),
    path('categories', views.categories, name='categories'),
    path('advertisements/', views.Advertisements.as_view()),
]