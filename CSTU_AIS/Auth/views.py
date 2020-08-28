from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from Auth.models import *
from Student.models import Student
import requests
import json

def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teacher_page')
        if request.user.is_student:
            return redirect('student_page')
        else:
            return redirect('staff_page')
    return render(request, 'home.html')

def login_ict(request):

    if request.method == "GET":
        return render(request, 'login_ict.html')

    stu_id = request.POST.get('user')
    psw = request.POST.get('pass')
    url = 'https://restapi.tu.ac.th/api/v1/auth/Ad/verify'
    body = {"UserName" : stu_id,"PassWord" : psw}
    headers = {'content-type': 'application/json',
               'application-key' : 'TUf969ac6e7051a35e4d05a29b3d6f404b8244ccca9926982b1f02295cb086a1bedd74e4c44a7729bfca293ec806fffbc4'
              }
    
    r = requests.post(url, data=json.dumps(body), headers=headers).json()
    first2 = stu_id[:2]
    if r.get('status')==True and r.get('department')=='ภาควิชาวิทยาการคอมพิวเตอร์' :
        if r.get('type')=='student':
            if User.objects.filter(username=stu_id).exists():
                old = User.objects.get(username=stu_id)
                stu = Student.objects.get(student_id=old)
                stu.status = r.get('tu_status')
                stu.save()
                user = authenticate(request, username=stu_id, password=psw)
                login(request, user)
                return redirect('student_page')
            else:
                new = User.objects.create_user(stu_id,password=psw)
                new.is_student = True
                new.save()
                stu = Student.objects.create(student_id=new)
                stu.name = r.get('displayname_th')
                stu.status = r.get('tu_status')
                stu.email= r.get('email')
                admit_year = 2500+first2
                stu.admit_year = admit_year
                if(first2 >= 56 and first2<61):
                    stu.curri = Curriculum.objects.get(curri=56)
                if(first2 >= 61): 
                    stu.curri = Curriculum.objects.get(curri=56)
                stu.save()
                user = authenticate(request, username=stu_id, password=psw)
                login(request, user)
                return redirect('student_page')
            return render(request, 'login_ict.html')
        else:
            return render(request, 'login_ict.html')
    else:
        return render(request, 'login_ict.html')    

