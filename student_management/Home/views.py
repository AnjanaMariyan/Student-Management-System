from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from Home.models import User,Teacher
from Home.form import StudentForm






# Create your views here.

def reg_redirect(request):
    return render(request,'reg_page.html')


def student_registration(request):
    if request.method=='POST':
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
       
        email=request.POST.get('email')
        phone=request.POST.get('ph')
        deprt=request.POST.get('dept')
        username=request.POST.get('uname')
        pasw=request.POST.get('psw')
        
        s=User.objects.create_user(first_name= firstname,last_name=lastname,email=email,username=username,phone=phone,usertype='student',department=deprt,password=pasw,is_superuser=0,is_staff=0,is_approved =1,is_active=1)
        s.save()
        return HttpResponse("<script>window.alert('Successfully Registered !!!!');window.location.href='/reg/'</script>")
    else:
        return render(request,'student_reg.html')  


def teacher_registration(request):
    if request.method=='POST':
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')

        email=request.POST.get('email')
        phone=request.POST.get('ph')
        deprt=request.POST.get('dept')
        username=request.POST.get('uname')
        pasw=request.POST.get('psw')
        
        r=User.objects.create_user(first_name= firstname,last_name=lastname,email=email,username=username,phone=phone,usertype='teacher',department=deprt,password=pasw,is_superuser=0,is_staff=1,is_approved=0,is_active=0)
        r.save()
        return HttpResponse("<script>window.alert('Successfully Registered !!!!');window.location.href='/reg/'</script>")
    else:
        return render(request,'teacher_reg.html')  

@login_required
def stuhome(request):
    return render(request,'student_home.html')

@login_required
def teacherhome(request):
    return render(request,'teacher_home.html')








@login_required
def det_stu(request,sid):
    stu=User.objects.get(id=sid)
    print(stu)
    stu.delete()
    return HttpResponse("<script>window.alert('Successfully Deleted !!!!');window.location.href='/adview/'</script>")

def sign_in(request):
    if request.method=='POST':
        uname=request.POST['uname']
        psw=request.POST['psw']
        stu=authenticate(request,username=uname,password=psw)
        if stu is not None:
            login(request,stu)
            if stu.is_superuser:
                return redirect("admin_home")


            elif stu.usertype == "student":
                request.session['stud_id']=stu.id
                return redirect(stuhome)
                return HttpResponse("<script>window.alert('Successfully Logged in !!!!')</script>")


            elif stu.usertype == "teacher" and stu.is_approved==1:
                request.session['t_id']=stu.id
                return redirect(teacherhome)
                return HttpResponse("<script>window.alert('Successfully Logged in !!!!')</script>")
        else:
            return HttpResponse("<script>window.alert('Invalid Username and Password !!!!')</script>")


    else:
        return render(request,'logins.html')



@login_required
def stud_edit_profile(request):
    if request.method=="GET":
        sid=request.session['stud_id']
        # data=User.objects.select_related('user_id').get(user_id=sid)
        
        data=User.objects.get(id=sid)
        print(data)

        return render(request,'student_profile_view.html',{'details':data})
    else:
        user_id = request.session.get('stud_id')
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        email=request.POST.get('email')
        phone=request.POST.get('ph')
        deprt=request.POST.get('dept')
        username=request.POST.get('uname')
        pasw=request.POST.get('psw')

        x=User.objects.get(id=user_id )
        x.first_name=firstname
        x.last_name=lastname
        x.email=email
        x.phone=phone
        x.department=deprt
        x.password=pasw
        x.save()
        return redirect('stuprofile')


@login_required
def teacher_comp(request):
    if request.method == 'POST':
        experience = request.POST.get('exp')
        salary = request.POST.get('salary')
        user = request.user
        
        s = Teacher.objects.create(user_id=user, experience=experience, salary=salary)
        s.save()
        return HttpResponse("<script>window.alert('Successfully Completed your profile!!!!');window.location.href='/th/'</script>")
    else:
        return render(request, 'comp_teacher_details.html')


@login_required
def admin_homepage(request):
    detail = User.objects.filter(usertype='student')
    detail1 = User.objects.filter(usertype='teacher')
    
    detail2 = Teacher.objects.select_related('user_id').all()

    

    return render(request, 'admin_view.html', {'data': detail, 'data1': detail1,'data2':detail2})





@login_required
def admin_approve_teacher(request, teacher_id):
   
    teacher =  User.objects.get(id=teacher_id, usertype='teacher')
    teacher.is_approved = 'True'
    teacher.is_active=1
    teacher.save()
    print(teacher)
    return HttpResponse("<script>window.alert('Successfully Approved!!!!');window.location.href='/adview/'</script>")

@login_required   
def admin_reject_teacher(request,teacher_id):
   
    teacher =  User.objects.get(id=teacher_id, usertype='teacher')
    teacher.delete()
    return HttpResponse("<script>window.alert('Successfully Rejected the application!!!!');window.location.href='/adview/'</script>")

@login_required
def teacher_view_profile(request):
        sid=request.session['t_id']
        data=Teacher.objects.select_related('user_id').get(user_id=sid)
        
        
     

        return render(request,'teacher_profile.html',{'details':data})


   
@login_required
def my_stud(request):
    
    teacher_user_id = request.session['t_id']
    teacher = Teacher.objects.get(user_id=teacher_user_id)
    department = teacher.user_id.department 
    students_in_department = User.objects.filter(department=department, usertype='student')
    return render(request, 'my_studs.html', {'students': students_in_department})
    
    


@login_required
def logouts(request):
    logout(request)
    # return redirect(sign_in)
    return HttpResponse("<script>window.alert('Successfully Logged out!!!!');window.location.href='/log/'</script>")


        

