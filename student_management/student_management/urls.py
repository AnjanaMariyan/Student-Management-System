# """
# URL configuration for student_management project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin
from django.urls import path,include
from Home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',views.reg_redirect),
    path('student/',views.student_registration),
    path('teacher/',views.teacher_registration, name='teacher'),
    path('log/',views.sign_in,name='logins'),
    path('adview/',views.admin_homepage,name='admin_home'),
    path('sth/',views. stuhome,name="student_homepage"),
    path('th/',views.teacherhome,name="teacher_homepage"),
    path('teacher_com/',views.teacher_comp,name="teacher_complete_profile"),
    path('stuedit/',views.stud_edit_profile,name='stuprofile'),
    path('stu_del/<int:sid>/',views.det_stu, name='delete_student'),
    path('approve_teacher/<int:teacher_id>/',views.admin_approve_teacher, name='admin_approve_teacher'),
    path('reject_teacher/<int:teacher_id>/',views.admin_reject_teacher, name='admin_reject_teacher'),
    path('tea_profile/', views.teacher_view_profile, name='teacher_view_profile'),
    path('mystud/', views.my_stud, name='mystudents'),
    path('lg/', views.logouts, name='signout'),


    


    
]
