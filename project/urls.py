from django.urls import path
from . import views
from courses import views as courses_view
from students import views as students_view
from staff import views as staffs_view
from enquiries import views as enquiries_view
from account.views import login as user_login, user_logout
from django.contrib.auth import views as auth_views

urlpatterns = [   

   # * Authentication
   path('', user_login, name='login'),
   path('logout/', user_logout, name='logout'),
   path('change_password/', auth_views.PasswordChangeView.as_view(template_name='account/change_password.html', success_url='/settings/'), name="change_password"),

   # * Dashboard
   path('dashboard/', views.dashboard, name='dashboard'),

   # * Courses
   path('courses/', courses_view.courses, name='courses'),
   path('course/<int:id>/', courses_view.course_detail, name="course_detail" ),
   path('course/<int:id>/delete/', courses_view.delete_course, name='delete_course'),

   # * Students
   path('students/', students_view.students, name='students'),

   # * Staff
   path('staffs/', staffs_view.staffs, name='staffs'),   

   # * Enquiries
   path('enquiries/', enquiries_view.enquiries, name='enquiries'),

   # * Search
   path('search/', views.search, name='search'),

   # * Admin Settings
   path('settings/', views.admin_settings, name='admin_settings'),
   
]