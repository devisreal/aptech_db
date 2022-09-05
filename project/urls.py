from django.urls import path
from project import views
from courses import views as courses_view
from students import views as students_view
from staff import views as staffs_view
from enquiries import views as enquiries_view
from account.views import edit_profile, login as user_login, user_logout
from django.contrib.auth import views as auth_views

urlpatterns = [   

   # * Authentication
   path('', user_login, name='login'),
   path('logout/', user_logout, name='logout'),
   path('change_password/', auth_views.PasswordChangeView.as_view(template_name='account/change_password.html', success_url='/settings/'), name="change_password"),
   path('edit_profile/', edit_profile, name="edit_profile"),

   # * Dashboard
   path('dashboard/', views.dashboard, name='dashboard'),

   # * Courses
   path('courses/', courses_view.courses, name='courses'),
   path('course/<int:id>/', courses_view.course_detail, name="course_detail" ),
   path('course/<int:id>/delete/', courses_view.delete_course, name='delete_course'),

   # * Students
   path('students/', students_view.students, name='students'),
   path('student/<slug:slug>/', students_view.student_detail, name='student_detail'),
   path('student/<slug:slug>/update/', students_view.update_student, name='update_student'),
   path('student/<slug:slug>/program_completed/', students_view.set_program_completed, name='program_completed'),
   path('student/<slug:slug>/delete/', students_view.delete_student, name='delete_student'),
   path('students/new/', students_view.register_student, name='new_student'),

   # * Staff
   path('staffs/', staffs_view.staffs, name='staffs'),   
   path('staff/<slug:slug>/', staffs_view.staff_detail, name="staff_detail"),
   path('staff/<slug:slug>/delete/', staffs_view.delete_staff, name="delete_staff"),

   # * Enquiries
   path('enquiries/', enquiries_view.enquiries, name='enquiries'),
   path('enquiries/new/', enquiries_view.add_enquiry, name='new_enquiry'),
   path('enquiry/<slug:slug>/', enquiries_view.enquiry_detail, name='enquiry_detail'),
   path('enquiry/<slug:slug>/delete/', enquiries_view.delete_enquiry, name="delete_enquiry"),
   path('enquiry/<slug:slug>/update/', enquiries_view.update_enquiry, name="update_enquiry"),

   # * Search
   path('search/', views.search, name='search'),

   # * Admin Settings
   path('settings/', views.admin_settings, name='admin_settings'),
   
]