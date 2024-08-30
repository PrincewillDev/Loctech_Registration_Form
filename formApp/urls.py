 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_reg, name='student_reg'),
    path('<uuid:student_id>/', views.student_reg, name='student_update'),
    path('delete/<uuid:student_id>/', views.student_delete, name='student_delete'),
    path('list/', views.student_list, name='student_list'),
]