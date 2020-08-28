from django.db import models
from Auth.models import User
from Course.models import Course,Curriculum
from Teacher.models import Teacher

class Title(models.Model):
    title = models.CharField(max_length = 50)
    def __str__(self):
        return self.title

class Parent(models.Model):
    title = models.CharField(max_length =100, default="")
    p_name = models.CharField(max_length = 50,null=True)
    p_surname = models.CharField(max_length = 50,null=True)
    p_relation = models.CharField(max_length = 50,null=True)
    p_phone = models.CharField(max_length = 11,null=True)
    p_income = models.FloatField(null=True)
    

class Entrance_Info (models.Model):
    high_school_plan  = models.CharField(max_length = 100,null=True)
    school = models.CharField(max_length = 200,null=True)
    province = models.CharField(max_length = 200,null=True)
    educaeted_year = models.IntegerField(null=True)
    entrance_score = models.FloatField(null=True)
    gat = models.FloatField(null=True)
    pat1 = models.FloatField(null=True)
    pat2 = models.FloatField(null=True)
    onet_th = models.FloatField(null=True)
    onet_sci = models.FloatField(null=True)
    onet_eng = models.FloatField(null=True)
    onet_soc = models.FloatField(null=True)
    onet_math = models.FloatField(null=True)
    gpax = models.FloatField(null=True)

class Student (models.Model):
    student_id = models.ForeignKey(User,on_delete = models.CASCADE)
    titles = models.CharField(max_length =200, default="")
    name = models.CharField(max_length =200, default="")
    surname = models.CharField(max_length = 50,default="")
    status = models.CharField(max_length =50,default="")
    curri = models.ForeignKey(Curriculum,on_delete = models.CASCADE,default=1)
    major_track = models.CharField(max_length = 100 ,default="")
    gpa = models.CharField(max_length = 20 ,default="") 
    email = models.EmailField(max_length = 50, default="")
    line_id = models.CharField(max_length = 50 ,default="")
    phone = models.CharField(max_length = 11 ,default="")
    address = models.TextField(max_length = 500, null=True,default="")
    adviser = models.ForeignKey(Teacher,on_delete = models.CASCADE, null=True)
    parent = models.ForeignKey(Parent,on_delete = models.CASCADE ,null=True)
    ent_info = models.ForeignKey(Entrance_Info,on_delete = models.CASCADE ,null=True)
    degree = models.CharField(max_length = 200, default="")
    campus = models.CharField(max_length = 200, default="")
    applicant_type_id = models.IntegerField(null=True)
    applicant_type = models.CharField(max_length = 200 ,null=True)
    admit_year = models.IntegerField(null=True)
    tcas = models.CharField(max_length = 200 ,null=True)
    def __str__(self):
        return str(self.student_id)


class Enrollment(models.Model):
    student_id = models.ForeignKey(Student,on_delete = models.CASCADE)
    course_id = models.CharField(max_length = 20)
    course_name = models.CharField(max_length = 200 ,default="")
    semester = models.CharField(max_length = 20)
    academic_year = models.IntegerField(null=True)
    grade = models.CharField(max_length = 20,null=True)
    credit = models.IntegerField(null=True)
    def __str__(self):
        return "{} - {} - {} ".format(str(self.course_id),str(self.semester),str(self.academic_year))
        #return "{} - {} - {} - {} ".format(str(self.student_id),self.course_id,self.semester,self.academic_year)

class Check_for_lastest(models.Model):
    student_id = models.ForeignKey(Student,on_delete = models.CASCADE,null=True)
    check_for_cs101 = models.ForeignKey(Enrollment,on_delete = models.CASCADE,related_name='check101',null=True)
    check_for_cs223 = models.ForeignKey(Enrollment,on_delete = models.CASCADE,related_name='check223',null=True)
    check_for_cs300 = models.ForeignKey(Enrollment,on_delete = models.CASCADE,related_name='check300',null=True)
