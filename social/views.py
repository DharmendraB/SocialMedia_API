from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
class HomeView(TemplateView):
    template_name = "social/home.html"
    
class AboutView(TemplateView):
    template_name = "social/about.html"
class ContactView(TemplateView):
    template_name = "social/contact.html"

@method_decorator(login_required, name="dispatch")
class ProfileUpdateView(UpdateView):
    template_name = "social/profile_form.html"
    model = User
     # Use this for all Field disply user
    fields = "__all__" 
