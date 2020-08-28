from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from Staff.views import *

urlpatterns = [
    path('course_upload', course_upload, name='course_upload'),
    
]