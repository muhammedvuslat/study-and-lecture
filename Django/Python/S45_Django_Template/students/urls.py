from django.urls import path
from .views import (
    home,
    student_list,
    student_add
    )


urlpatterns = [
    path('', home, name='home'),#! ana domainde views.py da bulunan home modülü çalışıyor
    path('list/', student_list, name='student_list'),
    path('list/', student_list, name='student_list'),
    path('add/', student_add, name='student_add'),
]
 