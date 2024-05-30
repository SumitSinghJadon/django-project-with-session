
from django.urls import path
from .views import *

urlpatterns =[
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('registration/',registration,name='registration'),
    path('registardata/',submit_registration,name='register'),
    path('login/',login,name='login'),
    path('submitlogin/',submitlogin,name='submitlogin'),
    path('logout/',logout,name='logout'),
    path('dashboard/',dashboard,name='dashboard'),
    path('submitnote/',submitnote,name='submitnote'),
    path('shownotes/',shownotes,name='shownotes'),
    path('delete/<int:pk>',delete,name='delete'),
    path('Edit/<int:pk>',Edit,name='Edit'),
    path('updatenote/<int:pk>',updatenote,name='updatenote'),
    path('filter/',filter,name='filter')
    
    
    
    
]
