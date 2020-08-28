from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    path('', view_for_teacher, name='teacher_page'),
    path('view_profile',view_teacher, name='view_teacher'),
    path('edit_profile', edit_teacher, name='edit_teacher'),
    path('create_profile', create_teacher, name='create_teacher'),
    path('view_dashboard',view_dashboard_t,name = 'view_dashboard_t'),
    path('view_dashboard2',view_dashboard2_t,name = 'view_dashboard2_t'),    

]