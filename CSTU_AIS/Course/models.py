from django.db import models

class Curriculum(models.Model):
    curri= models.IntegerField()  
    def __str__(self):
        return str(self.curri)

class Course(models.Model):
    course_id = models.CharField(max_length=20)
    curriculum = models.ForeignKey(Curriculum,on_delete=models.CASCADE,null=True)
    course_name = models.CharField(max_length=200,null=True)
    course_description = models.CharField(max_length=1000,null=True)
    credit = models.IntegerField(null=True )
    lecture_hours = models.IntegerField(null=True )
    lab_hours = models.IntegerField(null=True )
    selfstudy_hours = models.IntegerField(null=True)

    def __str__(self):
       return "{} - {}".format(self.course_id,self.curriculum)

class Prerequisite_Type(models.Model):
    description= models.CharField(max_length=20)  
    def __str__(self):
        return self.description 

class Prerequisite(models.Model):
    pre_course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='postreq_set',null=True)
    group = models.IntegerField(null=True)
    post_course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='prereq_set',null=True)
    pre_type = models.ForeignKey(Prerequisite_Type,on_delete=models.CASCADE,default=1 ,null=True)

    def __str__(self):
        return "[{}] {} -> {}".format(self.group,self.pre_course,self.post_course)

class usage_type(models.Model):
    usage_type = models.CharField(max_length=100)
    usage_condition = models.CharField(max_length=100)
   
    def __str__(self):
        return "{}  {}".format(self.usage_type,self.usage_condition)

class course_condition(models.Model):
    condition = models.CharField(max_length=100)
    def __str__(self):
        return self.condition

class major_or_track(models.Model):
    curriculum = models.ForeignKey(Curriculum,on_delete=models.CASCADE,null=True)
    major_or_track = models.CharField(max_length=100)
    def __str__(self):
        return "{} - {}".format(self.curriculum,self.major_or_track)

class course_sector_curriculum(models.Model):
    sector_no = models.IntegerField(null=True)
    sector_name = models.CharField(max_length=100)
    def __str__(self):
        return "{} - {}".format(self.curriculum,self.sector_no)

class course_sector_tgf(models.Model):
    tqf_sector_no = models.IntegerField(null=True)
    tqf_sector_name = models.CharField(max_length=200)
    def __str__(self):
        return "{} - {}".format(self.curriculum,self.tqf_sector_no)

class course_usage(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    major_or_track = models.ForeignKey(major_or_track,on_delete=models.CASCADE,null=True)
    elective_or_mandatory = models.ForeignKey(usage_type,on_delete=models.CASCADE,null=True)
    course_sector = models.ForeignKey(course_sector_curriculum,on_delete=models.CASCADE,null=True)
    course_tqf = models.ForeignKey(course_sector_tgf,on_delete=models.CASCADE,null=True)
    condition = models.ForeignKey(course_condition,on_delete=models.CASCADE,null=True)

    def __str__(self):
       return "{} ( {} )".format(self.course,self.major_or_track)

class Grade(models.Model):
    grade = models.CharField(max_length = 50)
    grade_value = models.FloatField()
    def __str__(self):
        return self.grade
