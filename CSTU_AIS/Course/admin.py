from django.contrib import admin
from Course.models import *


admin.site.register(Curriculum)
admin.site.register(Course)
admin.site.register(Prerequisite)
admin.site.register(Prerequisite_Type)
admin.site.register(usage_type)
admin.site.register(major_or_track)
admin.site.register(course_sector_curriculum)
admin.site.register(course_sector_tgf)
admin.site.register(course_usage)
admin.site.register(Grade)
