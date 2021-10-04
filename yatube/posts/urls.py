from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    path('group/', views.group),
    path('group/<slug:slug>/', views.group_posts)
] 