from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    path('', view_for_student, name='student_page'),
    path('view_profile',view_student, name='view_student'),
    path('edit_profile', update_student, name='edit_student'),
    path('create_student', create_student, name='create_student'),
    path('create_entrance_info', create_entance_info, name ='entrance'),
    path('view_enrollment',view_enrollment,name='view_enrollment'),
    path('add_enrollment',add_enrollment,name='add_enrollment'),


]