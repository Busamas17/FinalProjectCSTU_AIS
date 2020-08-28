from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    path('', view_for_staff, name='staff_page'),
    path('course_upload', course_upload, name='course_upload'),
    path('create_user', create_user, name='create_user'),
    path('teaher_upload',teacher_upload,name = 'teacher_upload'),
    path('enrollment_upload',enrollment_upload,name = 'enrollment_upload'),
    path('student_upload',add_student_info,name = 'student_upload'),
    path('view_dashboard',view_dashboard,name = 'view_dashboard'),
    path('view_dashboard2',view_dashboard2,name = 'view_dashboard2'),    
    path('view_dashboard2',view_dashboard2,name = 'view_dashboard2'),   
    path('search_student',search_student,name = 'search_student'),   

]