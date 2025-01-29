from django.urls import path
from . import views


app_name = 'lessons'


urlpatterns = [
    path('', views.lessons_list, name='list'),
    path('<int:pk>/', views.lesson_detail, name='detail'),
    path('delete/<int:pk>/', views.lesson_delete, name='delete'),
    path('create/', views.create_lesson, name='create'),
]
