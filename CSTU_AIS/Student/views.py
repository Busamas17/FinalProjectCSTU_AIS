from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect
from Student.models import *
from Student.models import Parent
from Auth.models import User
from Course.models import *
import json as simplejson

@user_passes_test(lambda u: u.is_student)
def view_for_student(request): 
    if Student.objects.filter(student_id=request.user.id).exists():
        ab = Student.objects.get(student_id=request.user.id)
        return render(request,'student_page.html',{'name' : ab.name })
    else:
        return HttpResponseRedirect('/student/create_student')

@user_passes_test(lambda u: u.is_student)
def view_student(request):
    ab = Student.objects.get(student_id=request.user.id)
    return render(request,'student_profile.html',{'data' : ab})

def view_enrollment(request):
    stu = Student.objects.get(student_id=request.user.id)
    ent = Enrollment.objects.filter(student_id=stu.id).order_by('academic_year','semester','course_id')
    context = { 
        'ent_1' : Enrollment.objects.filter(student_id=stu.id).filter(academic_year=stu.admit_year),
        'ent_2' : Enrollment.objects.filter(student_id=stu.id).filter(academic_year=stu.admit_year+1),
        'ent_3' : Enrollment.objects.filter(student_id=stu.id).filter(academic_year=stu.admit_year+2),
        'ent_4' : Enrollment.objects.filter(student_id=stu.id).filter(academic_year=stu.admit_year+3),
        'ent_5' : Enrollment.objects.filter(student_id=stu.id).filter(academic_year=stu.admit_year+4),
        'ent_6' : Enrollment.objects.filter(student_id=stu.id).filter(academic_year=stu.admit_year+5),
        'ent_7' : Enrollment.objects.filter(student_id=stu.id).filter(academic_year=stu.admit_year+6),
        'ent_8' : Enrollment.objects.filter(student_id=stu.id).filter(academic_year=stu.admit_year+7),
        'year' : stu.admit_year
    }
    return render(request,'student_view_enrollment.html',context)

def update_student(request):
    post = Student.objects.get(student_id=request.user.id)
    context = {
        'student' : post,
        'title' : Title.objects.all(),
        'advisor' : Teacher.objects.all(),
        'curri' : Curriculum.objects.all(),
    }
    if request.method == 'POST':
        par = Parent.objects.filter(id=post.parent_id)
        if par.count()<=0:
            par = Parent.objects.create(id=post.parent_id)
            par.save()
        else:
            par = Parent.objects.get(id=post.parent_id)
        if request.POST.get('address'):
            post.address= request.POST.get('address')
        if request.POST.get('phone'):
            post.phone= request.POST.get('phone')
        if request.POST.get('admit_year'):
            post.admit_year= request.POST.get('admit_year')
        if request.POST.get('degree'):
            post.degree= request.POST.get('degree')
        if request.POST.get('email'):
            post.email= request.POST.get('email')
        if request.POST.get('line_id'):
            post.line_id= request.POST.get('line_id')
        if request.POST.get('p_title'):
            if request.POST.get('p_title')!="0":
                par.title= request.POST.get('p_title')
        if request.POST.get('p_name'):
            par.p_name= request.POST.get('p_name')
        if request.POST.get('p_surname'):
            par.p_surname= request.POST.get('p_surname')
        if request.POST.get('p_relation'):
            par.p_relation= request.POST.get('p_relation')
        if request.POST.get('p_phone'):
            par.p_phone= request.POST.get('p_phone')
        if request.POST.get('p_income'):    
            par.p_income= request.POST.get('p_income')
        par.save()
        post.parent = par
        post.save()  
        messages.success(request, 'Profils has been update !')
        return HttpResponseRedirect('/student/view_profile')
    else:
        return render(request,'student_update.html', context)

def create_student(request):
    if request.method == 'POST':
        post = Student.objects.create(student_id=request.user)
        par = Parent.objects.create()
        if request.POST.get('title'):
            post.titles= request.POST.get('title')
        if request.POST.get('name'):
            post.name= request.POST.get('name')
        if request.POST.get('surname'):
            post.surname= request.POST.get('surname')
        if request.POST.get('status'):
            post.status= request.POST.get('status')
        if request.POST.get('curri'): 
            post.curri= Curriculum.objects.get(id=request.POST.get('curri'))
        if request.POST.get('major'):
            post.major_track= request.POST.get('major')
        if request.POST.get('address'):
            post.address= request.POST.get('address')
        if request.POST.get('gpa'):
            post.gpa= request.POST.get('gpa')
        if request.POST.get('degree'):
            post.degree= request.POST.get('degree')
        if request.POST.get('campus'):
            post.campus= request.POST.get('campus')
        if request.POST.get('phone'):
            post.phone= request.POST.get('phone')
        if request.POST.get('email'):
            post.email= request.POST.get('email')
        if request.POST.get('line_id'):
            post.line_id= request.POST.get('line_id')
        if request.POST.get('p_title'):
            par.title= request.POST.get('p_title')
        if request.POST.get('p_name'):
            par.p_name= request.POST.get('p_name')
        if request.POST.get('p_surname'):
            par.p_surname= request.POST.get('p_surname')
        if request.POST.get('p_relation'):
            par.p_relation= request.POST.get('p_relation')
        if request.POST.get('p_phone'):
            par.p_phone= request.POST.get('p_phone')
        if request.POST.get('p_income'):    
            par.p_income= request.POST.get('p_income')
        par.save()
        post.parent = par
        post.save()  

        return HttpResponseRedirect('profile_student.html')
    else:
        data = Title.objects.all()       
        return render(request,'create_student.html',{'data':data})

def create_entance_info(request):
    
    if request.method == 'GET':
        post = Student.objects.get(student_id=request.user)
        if(post.curri.id == 2):
            return render(request,'student_ent_score61.html')
        else:
            return render(request,'student_ent_score56.html')
    if request.method == 'POST':
        post = Student.objects.get(student_id=request.user)
        if Entrance_Info.objects.filter(id=post.ent_info_id).exists():
            ent_info = Entrance_Info.objects.get(id=post.ent_info_id)
            if request.POST.get('school'):   
                ent_info.school= request.POST.get('school')
            if request.POST.get('pro_school'):   
                ent_info.province= request.POST.get('pro_school')
            if request.POST.get('plan'):  
                if request.POST.get('plan')!="0": 
                    ent_info.high_school_plan= request.POST.get('plan')
            if request.POST.get('educaeted_year'):   
                ent_info.educaeted_year= request.POST.get('educaeted_year')    
            if request.POST.get('gpax'):   
                ent_info.gpax= request.POST.get('gpax')
            if request.POST.get('tcas'):   
                if request.POST.get('tcas')!="0":
                    post.tcas= request.POST.get('tcas')
            if request.POST.get('onet_th'):   
                ent_info.onet_th= request.POST.get('onet_th')
            if request.POST.get('onet_soc'):   
                ent_info.onet_soc= request.POST.get('onet_soc')
            if request.POST.get('onet_eng'):   
                ent_info.onet_eng= request.POST.get('onet_eng')
            if request.POST.get('onet_math'):   
                ent_info.onet_math= request.POST.get('onet_math')
            if request.POST.get('onet_sci'):   
                ent_info.onet_sci= request.POST.get('onet_sci')
            if request.POST.get('gat'):   
                ent_info.gat= request.POST.get('gat')
            if request.POST.get('pat1'):   
                ent_info.pat1= request.POST.get('pat1')
            if request.POST.get('pat2'):   
                ent_info.pat2= request.POST.get('pat2')
            if request.POST.get('entrance_score'):   
                ent_info.entrance_score= request.POST.get('entrance_score')
            ent_info.save()
            post.ent_info = ent_info
            post.save()
        
        else:
            ent_info = Entrance_Info.objects.create()
            if request.POST.get('school'):   
                ent_info.school= request.POST.get('school')
            if request.POST.get('pro_school'):   
                ent_info.province= request.POST.get('pro_school')
            if request.POST.get('plan'):
                if request.POST.get('plan')!="0":   
                    ent_info.high_school_plan= request.POST.get('plan')
            if request.POST.get('educaeted_year'):   
                ent_info.educaeted_year= request.POST.get('educaeted_year')    
            if request.POST.get('gpax'):   
                ent_info.gpax= request.POST.get('gpax')
            if request.POST.get('tcas'):   
                if request.POST.get('tcas')!="0":
                    post.tcas= request.POST.get('tcas')
            if request.POST.get('onet_th'):   
                ent_info.onet_th= request.POST.get('onet_th')
            if request.POST.get('onet_soc'):   
                ent_info.onet_soc= request.POST.get('onet_soc')
            if request.POST.get('onet_eng'):   
                ent_info.onet_eng= request.POST.get('onet_eng')
            if request.POST.get('onet_math'):   
                ent_info.onet_math= request.POST.get('onet_math')
            if request.POST.get('onet_sci'):   
                ent_info.onet_sci= request.POST.get('onet_sci')
            if request.POST.get('gat'):   
                ent_info.gat= request.POST.get('gat')
            if request.POST.get('pat1'):   
                ent_info.pat1= request.POST.get('pat1')
            if request.POST.get('pat2'):   
                ent_info.pat2= request.POST.get('pat2')
            if request.POST.get('entrance_score'):   
                ent_info.entrance_score= request.POST.get('entrance_score')
            ent_info.save()
            post.ent_info = ent_info
            post.save()
        
        return HttpResponseRedirect('/student')

def add_enrollment(request): 
    post = Student.objects.get(student_id=request.user)
    context = {
            'grade' : Grade.objects.all(),
            'year' : post.admit_year,
            'course' : Course.objects.filter(curriculum_id=post.curri_id).order_by('course_id')
        }
    if request.method == 'POST':
        i=1
        while i <= int(request.POST.get('count')):
            sub='subj'+str(i)
            sem='sem'+str(i)
            year='year'+str(i)
            grade='grade'+str(i)
            if request.POST.get(sub):
                if  (Enrollment.objects.filter(student_id=post).filter(course_id=request.POST.get(sub)).filter(semester = request.POST.get(sem)).filter(academic_year=int(request.POST.get(year))).exists()):
                    messages.error(request, 'Duplicated data !')
                    return  render(request,'student_add_enrollment.html',context)
                else:
                    get_name = Course.objects.get(curriculum_id=post.curri_id,course_id=request.POST.get(sub))
                    ent = Enrollment.objects.create(student_id=post) 
                    ent.course_id = request.POST.get(sub)
                    ent.course_name = get_name.course_name
                    ent.semester = request.POST.get(sem)
                    ent.academic_year = int(request.POST.get(year))
                    ent.grade = request.POST.get(grade)
                    ent.save()
                    if ent.course_id=="CS101":
                        last_enroll=Enrollment.objects.filter(student_id=post).filter(course_id="CS101").order_by('academic_year','semester').last()
                        post.check_for_cs101=last_enroll.grade
                        post.save()
                    if ent.course_id=="CS300":
                        last_enroll=Enrollment.objects.filter(student_id=post).filter(course_id="CS300").order_by('academic_year','semester').last()
                        post.check_for_cs223=last_enroll.grade
                        post.save()
                    if ent.course_id=="CS223":
                        last_enroll=Enrollment.objects.filter(student_id=post).filter(course_id="CS223").order_by('academic_year','semester').last()
                        post.check_for_cs300=last_enroll.grade
                        post.save()
            i=i+1
        messages.success(request, "Enrollment has been update !")
        return render(request,'student_add_enrollment.html', context)
    else:
        return render(request,'student_add_enrollment.html', context)


