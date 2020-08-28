from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Teacher



@user_passes_test(lambda u: u.is_teacher)
def view_for_teacher(request): 
    if Teacher.objects.filter(teacher_id=request.user.id).exists():
        ab = Teacher.objects.get(teacher_id=request.user.id)
        return render(request,'teacher_page.html',{'name' : ab })
    else:
        return HttpResponseRedirect('/teacher/create_profile')

@user_passes_test(lambda u: u.is_teacher)
def view_teacher(request):
    ab = Teacher.objects.get(teacher_id=request.user.id)
    return render(request,'profile_teacher.html',{'data' : ab })

def view_dashboard_t(request):
    return render(request,'dashboard1_teacher.html')

def view_dashboard2_t(request):
    return render(request,'dashboard2_teacher.html')

@user_passes_test(lambda u: u.is_teacher)
def create_teacher(request):
    if request.method == 'POST':
        post = Teacher.objects.create(teacher_id=request.user)
        if request.POST.get('name'):
            post.name= request.POST.get('name')
        if request.POST.get('surname'):
            post.surname= request.POST.get('surname')
        if request.POST.get('ac_pst'):
            post.academic_position= request.POST.get('ac_pst')
        if request.POST.get('mng_pst'):
            post.management_position= request.POST.get('mng_pst')
        if request.POST.get('edc'):
            post.education= request.POST.get('edc')
        if request.POST.get('works'):
            post.works= request.POST.get('works')
        post.save()  
        return HttpResponseRedirect('/teacher/view_profile')
    else:
        return render(request,'create_teacher.html')

@user_passes_test(lambda u: u.is_teacher)
def edit_teacher(request):
    if request.method == 'POST':
        post = Teacher.objects.get(teacher_id=request.user.id)
        if request.POST.get('aca'):
            if request.POST.get('aca')!="0": 
                post.academic_position= request.POST.get('aca')
        if request.POST.get('edu'):
            if request.POST.get('edu')!="0": 
                post.education_position= request.POST.get('edu')
        if request.POST.get('name'):
            post.name= request.POST.get('name')
        if request.POST.get('surname'):
            post.surname= request.POST.get('surname')
        if request.POST.get('edc'):
            post.education= request.POST.get('edc')
        if request.POST.get('works'):
            post.works= request.POST.get('works')
        post.save()  
        messages.success(request, 'Profils has been update !')
        return HttpResponseRedirect('/teacher/view_profile')
    else:
        return render(request,'edit_teacher.html')


