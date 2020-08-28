from django.db import models
from Auth.models import User
    

class Teacher(models.Model):
    teacher_id = models.ForeignKey(User,on_delete = models.CASCADE)
    academic_position = models.CharField(max_length = 20, default="",null=True)
    education_position = models.CharField(max_length = 20, default="",null=True)
    name = models.CharField(max_length = 50,null=True)
    surname = models.CharField(max_length = 50,null=True)
    email = models.EmailField(null=True)
    education = models.CharField(max_length = 500, default="")
    works = models.CharField(max_length = 500,null=True,default="")
    campus = models.CharField(max_length = 50,null=True)
    status = models.CharField(max_length = 50,null=True)
    def __str__(self):
        return self.name