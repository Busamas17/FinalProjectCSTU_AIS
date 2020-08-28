from django.contrib import admin
from .models import *

class StudentInline(admin.TabularInline):
  model = Enrollment

class StudentAdmin(admin.ModelAdmin):
  list_display = ('student_id',)
  search_fields = ['student_id']
  inlines = (StudentInline,)
  ordering = ('student_id',)

admin.site.register(Title)
admin.site.register(Student, StudentAdmin)
admin.site.register(Parent)
admin.site.register(Entrance_Info)
admin.site.register(Enrollment)

