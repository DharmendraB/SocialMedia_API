from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from social import views

urlpatterns = [
     path('home/', views.HomeView.as_view()),
     path('about/', views.AboutView.as_view()),
     path('contact/', views.ContactView.as_view()),
     path('', RedirectView.as_view(url="home/")),
     path('profile/edit/<int:pk>/', views.ProfileUpdateView.as_view(success_url="/social/")),  

    # path('mylist/', views.MyList.as_view()),
    # path('notice/<int:pk>/', views.NoticeDetailtView.as_view()),
    # path('question/create/', views.QuestionCreate.as_view(success_url="/college/")),
    # path('profile/edit/<int:pk>/', views.ProfileUpdateView.as_view(success_url="/college/")),
]
