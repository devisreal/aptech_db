from django.urls import path
from . import views
from account.views import login as user_login, user_logout

urlpatterns = [   
   path('', user_login, name='login'),
   path('logout/', user_logout, name='logout'),
   path('dashboard/', views.dashboard, name='dashboard'),
   path('courses/', views.courses, name='courses'),
   path('students/', views.students, name='students'),
   path('staffs/', views.staffs, name='staffs'),   
   path('enquiries/', views.enquiries, name='enquiries'),


   path('search/', views.search, name='search'),
]