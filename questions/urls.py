from django.urls import path
from . import views


app_name = 'questions'


urlpatterns = [
    path('create/', views.create_test, name='create'),
    path('list/', views.test_list, name='list'),
    path('delete/<int:pk>/', views.test_delete, name='delete'),
    path('update/<int:pk>/', views.update_test, name='update'),
    path('detail/<int:pk>/', views.test_detail, name='detail'),
]
