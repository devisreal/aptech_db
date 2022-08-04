from django.urls import path
from . import views

urlpatterns = [   
   path('', views.login, name='login'),
   path('dashboard/', views.dashboard, name='dashboard'),
   path('courses/', views.courses, name='courses'),
   path('students/', views.students, name='students'),
   path('faculty/', views.faculty, name='faculty'),   
]