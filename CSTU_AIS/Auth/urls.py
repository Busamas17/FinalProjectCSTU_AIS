from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    path('', home,name = 'home'),
    path('login',login_ict, name = 'ict'),

]