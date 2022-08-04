from django.urls import path
from . import views

urlpatterns = [   
   path('', views.login, name='login'),
   path('dashboard/', views.dashboard, name='dashboard'),
   path('courses/', views.courses, name='courses'),
   path('students/', views.students, name='students'),
   path('staffs/', views.staffs, name='staffs'),   
   path('enquiries/', views.enquiries, name='enquiries')
]