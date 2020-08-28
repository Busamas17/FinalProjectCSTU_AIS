from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('Staff.urls')),
    path('staff/', include('Staff.urls')),
    path('teacher/', include('Teacher.urls')),
    path('student/', include('Student.urls')),
    path('course/', include('Course.urls')),
    path('home/',include('Auth.urls'),name='home'),
]


